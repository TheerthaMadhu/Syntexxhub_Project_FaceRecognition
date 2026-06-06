from flask import Flask, render_template, Response
import cv2
import face_recognition
import os
import numpy as np

app = Flask(__name__)

known_face_encodings = []
known_face_names = []

# Load known faces
path = "known_faces"

for file in os.listdir(path):
    img = face_recognition.load_image_file(
        os.path.join(path, file)
    )

    encodings = face_recognition.face_encodings(img)

    if len(encodings) > 0:
        known_face_encodings.append(encodings[0])
        known_face_names.append(
            os.path.splitext(file)[0]
        )

camera = cv2.VideoCapture(0)

def generate_frames():

    while True:

        success, frame = camera.read()

        if not success:
            break

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        face_locations = face_recognition.face_locations(rgb)
        face_encodings = face_recognition.face_encodings(
            rgb,
            face_locations
        )

        for (top, right, bottom, left), face_encoding in zip(
            face_locations,
            face_encodings
        ):

            matches = face_recognition.compare_faces(
                known_face_encodings,
                face_encoding
            )

            name = "Unknown"

            face_distances = face_recognition.face_distance(
                known_face_encodings,
                face_encoding
            )

            if len(face_distances) > 0:

                best_match_index = np.argmin(face_distances)

                if matches[best_match_index]:
                    name = known_face_names[best_match_index]

            cv2.rectangle(
                frame,
                (left, top),
                (right, bottom),
                (0, 255, 0),
                2
            )

            cv2.putText(
                frame,
                name,
                (left, top - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 255, 0),
                2
            )

        ret, buffer = cv2.imencode('.jpg', frame)

        frame = buffer.tobytes()

        yield (
            b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n'
            + frame +
            b'\r\n'
        )

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video')
def video():
    return Response(
        generate_frames(),
        mimetype='multipart/x-mixed-replace; boundary=frame'
    )

if __name__ == "__main__":
    app.run(debug=True)