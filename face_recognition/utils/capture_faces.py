import cv2
import numpy as np
import pickle
import os

def capture_faces(name):

    video = cv2.VideoCapture(0)

    facedetect = cv2.CascadeClassifier(
        cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
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

    faces_data = np.asarray(faces_data).reshape(100,-1)

    if not os.path.exists("data"):
        os.makedirs("data")

    if 'names.pkl' not in os.listdir('data'):

        names=[name]*100

        with open('data/names.pkl','wb') as f:
            pickle.dump(names,f)

        with open('data/faces_data.pkl','wb') as f:
            pickle.dump(faces_data,f)

    else:

        with open('data/names.pkl','rb') as f:
            names=pickle.load(f)

        names=names+[name]*100

        with open('data/names.pkl','wb') as f:
            pickle.dump(names,f)

        with open('data/faces_data.pkl','rb') as f:
            faces=pickle.load(f)

        faces=np.append(faces,faces_data,axis=0)

        with open('data/faces_data.pkl','wb') as f:
            pickle.dump(faces,f)