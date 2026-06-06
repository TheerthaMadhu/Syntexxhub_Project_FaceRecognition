import cv2
import os

name = input("Enter Name: ")

cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()

    cv2.imshow("Capture Face", frame)

    key = cv2.waitKey(1)

    if key == ord('s'):

        cv2.imwrite(
            f"known_faces/{name}.jpg",
            frame
        )

        print("Saved")
        break

cap.release()
cv2.destroyAllWindows()