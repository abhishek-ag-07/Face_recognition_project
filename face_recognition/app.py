import streamlit as st
import cv2
import numpy as np
import pickle
import os
import sqlite3
import pandas as pd
from datetime import datetime
from sklearn.neighbors import KNeighborsClassifier

st.set_page_config(page_title="Face Recognition Attendance System", layout="wide")

# -----------------------------
# DATABASE SETUP
# -----------------------------
conn = sqlite3.connect("attendance.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS attendance (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
date TEXT,
time TEXT
)
""")

conn.commit()

# -----------------------------
# LOAD FACE MODEL
# -----------------------------
def load_model():

    if not os.path.exists("data/names.pkl"):
        return None

    with open("data/names.pkl","rb") as f:
        labels = pickle.load(f)

    with open("data/faces_data.pkl","rb") as f:
        faces = pickle.load(f)

    knn = KNeighborsClassifier(n_neighbors=5)

    knn.fit(faces, labels)

    return knn

# -----------------------------
# CAPTURE FACES FUNCTION
# -----------------------------
def capture_faces(name):

    video = cv2.VideoCapture(0)

    facedetect = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )

    faces_data = []
    i = 0

    while len(faces_data) < 100:

        ret, frame = video.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = facedetect.detectMultiScale(gray,1.3,5)

        for (x,y,w,h) in faces:

            crop = frame[y:y+h, x:x+w]

            resized = cv2.resize(crop,(50,50))

            faces_data.append(resized)

            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

        cv2.imshow("Capturing Faces",frame)

        if cv2.waitKey(1) == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()

    faces_data = np.asarray(faces_data)
    faces_data = faces_data.reshape(100,-1)

    if not os.path.exists("data"):
        os.makedirs("data")

    if 'names.pkl' not in os.listdir('data'):

        names = [name]*100

        with open('data/names.pkl','wb') as f:
            pickle.dump(names,f)

        with open('data/faces_data.pkl','wb') as f:
            pickle.dump(faces_data,f)

    else:

        with open('data/names.pkl','rb') as f:
            names = pickle.load(f)

        names = names + [name]*100

        with open('data/names.pkl','wb') as f:
            pickle.dump(names,f)

        with open('data/faces_data.pkl','rb') as f:
            faces = pickle.load(f)

        faces = np.append(faces, faces_data, axis=0)

        with open('data/faces_data.pkl','wb') as f:
            pickle.dump(faces,f)

# -----------------------------
# MARK ATTENDANCE
# -----------------------------
def mark_attendance(name):

    ts = datetime.now()

    date = ts.strftime("%d-%m-%Y")
    time = ts.strftime("%H:%M:%S")

    cursor.execute(
        "SELECT * FROM attendance WHERE name=? AND date=?",
        (name,date)
    )

    result = cursor.fetchone()

    if result is None:

        cursor.execute(
            "INSERT INTO attendance (name,date,time) VALUES (?,?,?)",
            (name,date,time)
        )

        conn.commit()

# -----------------------------
# STREAMLIT UI
# -----------------------------
st.title("🎓 Face Recognition Attendance System")

menu = st.sidebar.selectbox(
    "Navigation",
    ["Register Student","Take Attendance","View Attendance"]
)

# -----------------------------
# REGISTER STUDENT
# -----------------------------
if menu == "Register Student":

    st.header("Register New Student")

    name = st.text_input("Enter Student Name")

    if st.button("Capture Face Dataset"):

        if name == "":
            st.warning("Please enter name")

        else:
            capture_faces(name)
            st.success("Face dataset captured successfully")

# -----------------------------
# TAKE ATTENDANCE
# -----------------------------
elif menu == "Take Attendance":

    st.header("Start Attendance")

    start = st.button("Start Camera")

    if start:

        knn = load_model()

        if knn is None:
            st.error("No dataset found. Please register student first.")
            st.stop()

        facedetect = cv2.CascadeClassifier(
            cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
        )

        video = cv2.VideoCapture(0)

        frame_placeholder = st.empty()

        while True:

            ret, frame = video.read()

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            faces = facedetect.detectMultiScale(gray,1.3,5)

            for (x,y,w,h) in faces:

                face = frame[y:y+h, x:x+w]

                resized = cv2.resize(face,(50,50)).flatten().reshape(1,-1)

                output = knn.predict(resized)

                name = output[0]

                mark_attendance(name)

                cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

                cv2.putText(frame,name,(x,y-10),
                            cv2.FONT_HERSHEY_SIMPLEX,1,
                            (255,255,255),2)

            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            frame_placeholder.image(frame)

# -----------------------------
# VIEW ATTENDANCE
# -----------------------------
elif menu == "View Attendance":

    st.header("Attendance Dashboard")

    df = pd.read_sql_query(
        "SELECT * FROM attendance",
        conn
    )

    st.dataframe(df)

    st.subheader("Attendance Chart")

    st.bar_chart(df["name"].value_counts())

