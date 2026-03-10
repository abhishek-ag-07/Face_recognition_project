# 🎓 Face Recognition Based Smart Attendance System

A **Face Recognition Attendance System** built using **Python, OpenCV, and Machine Learning (KNN)** that automatically detects and recognizes faces from a webcam and marks attendance.

The system captures face data, trains a recognition model, and records attendance with timestamps. A **Streamlit dashboard** displays attendance records in real time.

---

# 🚀 Features

✅ Face Detection using **OpenCV Haar Cascades**
✅ Face Recognition using **K-Nearest Neighbors (KNN)**
✅ Automatic **Attendance Recording**
✅ **Real-Time Webcam Detection**
✅ **Streamlit Dashboard for Attendance Visualization**
✅ **Voice Notification for Attendance Confirmation**
✅ Attendance stored **date-wise in CSV format**

---

# 🛠 Tech Stack

| Technology   | Purpose                |
| ------------ | ---------------------- |
| Python       | Programming Language   |
| OpenCV       | Face Detection         |
| NumPy        | Numerical Computations |
| Scikit-Learn | Machine Learning (KNN) |
| Streamlit    | Dashboard UI           |
| Pandas       | Data Handling          |

---

# 📂 Project Structure

```id="g1d2f4"
face_recognition_project
│
├── Attendance
│   └── Attendance_<date>.csv
│
├── data
│   ├── faces_data.pkl
│   └── names.pkl
│
├── add_faces.py
├── test.py
├── app.py
├── background.png
└── README.md
```

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/your-username/face-recognition-attendance-system.git
```

Move to project directory

```bash
cd face-recognition-attendance-system
```

Install dependencies

```bash
pip install opencv-python numpy pandas scikit-learn streamlit pywin32
```

---

# ▶️ How to Run

## 1️⃣ Capture Face Dataset

```bash
python add_faces.py
```

Enter your name and allow the webcam to capture **100 face images**.

---

## 2️⃣ Run Face Recognition

```bash
python test.py
```

Controls:

| Key   | Action          |
| ----- | --------------- |
| **o** | Mark attendance |
| **q** | Quit program    |

Attendance will be saved in the **Attendance folder**.

---

## 3️⃣ View Attendance Dashboard

```bash
streamlit run app.py
```

Open in browser:

```id="p3k7sa"
http://localhost:8501
```

---

# 📊 Example Attendance Output

```id="8k6b2d"
NAME,TIME
Abhishek,10:30:21
Rahul,10:32:10
```

---

# 🔮 Future Improvements

🚀 Deep Learning based face recognition (FaceNet / Dlib)
🚀 Database integration (MongoDB / MySQL)
🚀 Web-based attendance portal
🚀 Cloud deployment
🚀 Multiple user detection

---

# 👨‍💻 Author

**Abhishek Agarwal**

🎓 IT Undergraduate
💡 Interested in **Machine Learning, Open Source, and Full Stack Development**

---