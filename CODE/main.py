import cv2 
from deepface import DeepFace 

Screen = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

while Screen.isOpened():
    _, frame = Screen.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    for x, y, w, h in face:
        img = cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 3)
        try:
            analyze = DeepFace.analyze(frame, ['emotion'])
            cv2.putText(img, analyze[0]["dominant_emotion"], (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            print(analyze)
            print(analyze[0]["dominant_emotion"])
        except:
            print("no face")

    cv2.imshow('Screen', frame)
    key = cv2.waitKey(10)
    if key == ord('q'):
        break
Screen.release()