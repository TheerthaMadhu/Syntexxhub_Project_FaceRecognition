# Face Recognition Web Application

A real-time Face Recognition Web Application built using **Python**, **Flask**, **OpenCV**, and the **face_recognition** library. This project can detect and recognize multiple faces through a webcam and display the person's name on the screen.

---

## 📌 Features

* Real-time face detection using webcam
* Face recognition using face encodings
* Supports multiple known faces
* Displays bounding boxes around detected faces
* Labels recognized faces with names
* Add new users easily by saving their photos
* Simple Flask web interface
* Beginner-friendly project structure

---

## 🛠️ Technologies Used

* Python 3.x
* Flask
* OpenCV
* face_recognition
* NumPy
* HTML/CSS

---

## 📂 Project Structure

```text
FaceRecognitionWeb/
│
├── app.py
├── register.py
├── requirements.txt
│
├── known_faces/
│   ├── John.jpg
│   ├── Alice.jpg
│
├── static/
│   └── styles.css
│
└── templates/
    └── index.html
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/FaceRecognitionWeb.git
cd FaceRecognitionWeb
```

### 2. Create Virtual Environment (Optional)

```bash
python -m venv venv
```

Activate the environment:

Windows

```bash
venv\Scripts\activate
```

Linux/Mac

```bash
source venv/bin/activate
```

### 3. Install Required Libraries

```bash
pip install -r requirements.txt
```

---

## 📦 Requirements

```txt
Flask
opencv-python
face_recognition
numpy
```

---

## 🚀 Running the Application

Start the Flask server:

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

Allow webcam access if prompted.

---

## 👤 Adding New Faces

Place clear images inside the `known_faces` folder.

Example:

```text
known_faces/
├── Theertha.jpg
├── Rahul.jpg
├── Priya.jpg
```

The filename becomes the recognized person's name.

Example:

```text
Theertha.jpg
```

Output:

```text
Theertha
```

---

## 📸 Registering New Users

Run:

```bash
python register.py
```

Enter a name when prompted:

```text
Enter Name: Arun
```

Press **S** to capture and save the image.

The image will automatically be stored as:

```text
known_faces/Arun.jpg
```

Restart the application to load the new face.

---

## 🎯 How It Works

1. Loads images from the `known_faces` folder.
2. Converts each face into a numerical face encoding.
3. Captures video from the webcam.
4. Detects faces in each frame.
5. Compares detected faces with stored encodings.
6. Displays the recognized person's name above the face.

---

## 📷 Sample Output

```text
+--------------------+
|                    |
|      FACE          |
|                    |
+--------------------+

      John
```

Unknown faces are labeled as:

```text
Unknown
```

---

## 🔮 Future Enhancements

* Face Attendance System
* Database Integration (MySQL/MongoDB)
* Face Recognition History
* User Authentication
* Cloud Deployment
* Dark Mode UI
* Face Recognition from Uploaded Images
* Admin Dashboard

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a new branch
3. Commit your changes
4. Push to your branch
5. Create a Pull Request

---

## 📜 License

This project is developed for educational and internship purposes.

---

## 👨‍💻 Author

**Theertha Madhu**

SyntexxHub Internship Project - Face Detection & Recognition using OpenCV and Flask.
