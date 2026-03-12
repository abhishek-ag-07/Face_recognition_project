# 🎓 Face Recognition Smart Attendance System (Streamlit Edition)

A **Face Recognition Attendance System** built using **Python, OpenCV, Machine Learning, and Streamlit** that automatically detects faces, recognizes students, and records attendance in a database.

This project is an **enhanced version of the earlier Face Recognition Attendance System**, redesigned to run entirely on a **single Streamlit platform with database support and analytics dashboard**.

---

# 🚀 Key Improvements Over Previous Version

| Previous Version                                       | New Enhanced Version                              |
| ------------------------------------------------------ | ------------------------------------------------- |
| Multiple scripts (`add_faces.py`, `test.py`, `app.py`) | **Single Streamlit application (`app.py`)**       |
| Attendance stored in **CSV files**                     | Attendance stored in **SQLite database**          |
| Command-line execution                                 | **Web-based UI with Streamlit**                   |
| Separate face capture script                           | **Integrated student registration system**        |
| Basic recognition system                               | **Real-time recognition dashboard**               |
| No attendance analytics                                | **Live attendance charts and data visualization** |
| Duplicate attendance possible                          | **Duplicate attendance prevention**               |

---

# 🧠 System Workflow

1. **Register Student**

   * Capture face dataset via webcam
   * Store face features for training

2. **Take Attendance**

   * Detect and recognize faces in real-time
   * Automatically record attendance

3. **View Attendance**

   * View attendance table
   * Visualize attendance analytics

---

# 🛠 Tech Stack

| Technology             | Purpose                   |
| ---------------------- | ------------------------- |
| **Python**             | Core programming language |
| **OpenCV**             | Face detection            |
| **Scikit-Learn (KNN)** | Face recognition model    |
| **NumPy**              | Data processing           |
| **Streamlit**          | Web-based interface       |
| **SQLite**             | Attendance database       |
| **Pandas**             | Data analysis             |

---

# 📂 Project Structure

```
face_recognition_system
│
├── app.py                 # Main Streamlit application
├── attendance.db          # SQLite attendance database
│
├── data
│   ├── faces_data.pkl     # Stored face embeddings
│   └── names.pkl          # Labels for faces
│
└── README.md
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/your-username/face-recognition-attendance-system.git
```

Navigate into the project

```bash
cd face-recognition-attendance-system
```

Install required dependencies

```bash
pip install opencv-python numpy pandas scikit-learn streamlit
```

---

# ▶️ Running the System

Start the Streamlit application

```bash
streamlit run app.py
```

Open the application in your browser

```
http://localhost:8501
```

---

# 📌 How to Use

### 1️⃣ Register Student

* Enter the student's name
* Capture ~100 face samples using webcam

### 2️⃣ Take Attendance

* Start camera
* System recognizes faces automatically
* Attendance stored in database

### 3️⃣ View Attendance

* Display attendance records
* View attendance analytics charts

---

# 📊 Example Attendance Table

| ID | Name     | Date       | Time  |
| -- | -------- | ---------- | ----- |
| 1  | Abhishek | 12-03-2026 | 14:22 |
| 2  | Rahul    | 12-03-2026 | 14:25 |

---

# 📈 Attendance Dashboard

The Streamlit dashboard provides:

* Attendance data table
* Student attendance frequency chart
* Real-time updates

---

# 🔮 Future Improvements

* Deep Learning Face Recognition (FaceNet / Dlib)
* Multi-face recognition optimization
* Cloud deployment
* Admin login system
* Mobile attendance monitoring
* Email notifications for attendance

---

# 👨‍💻 Author

**Abhishek Agarwal**

🎓 IT Undergraduate
💡 Interested in **Machine Learning, Open Source, and Full Stack Development**

---

# ⭐ Support

If you like this project, consider **starring the repository** to support development!
