import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt.xml')

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale (gray, scaleFactor=1.5, minNeighbors=3)
    for (x, y, w, h) in faces:
        #print(x, y, w, h)
        roi_gray = gray[y:y+h, x:x+w]  # (ycord_start, ycord_end)
        roi_color = frame[y:y+h, x:x+w]
        
        color = (255, 255, 0)
        stroke = 1
        end_cord_x = x + w
        end_cord_y = y + h   
        cv2.rectangle(frame, (x, y), (end_cord_x, end_cord_y), color, stroke)

        centerX = str(round(int(x+(x+w)/2)))
        centerY = str(round(int(y+(y+h)/2)))

        ArduinoData = str(centerX + centerY)

        print(ArduinoData)

    cv2.imshow('frame', frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
