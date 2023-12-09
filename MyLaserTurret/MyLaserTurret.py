import numpy as np
import cv2
import time
import serial

ArduinoSerial = serial.Serial('com3', 115200)  #Specify the correct COM port

face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')

cap = cv2.VideoCapture(0)

prevposData = 000000

#---------------------------------------------------------------------------

while True:

    # Capture frame-by-frame  
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale (gray, scaleFactor=2, minNeighbors=3)

    for (x, y, w, h) in faces:
        #print(x, y, w, h)
        roi_gray = gray[y:y+h, x:x+w]  # (ycord_start, ycord_end)
        roi_color = frame[y:y+h, x:x+w]
        
        color = (255, 255, 0)
        stroke = 1
        end_cord_x = x + w
        end_cord_y = y + h   
        cv2.rectangle(frame, (x, y), (end_cord_x, end_cord_y), color, stroke)

        CenterX = str((x+(x+w))//2)
        CenterY = str((y+(y+h))//2)

#---------------------------------------------------------------------------

        if len(CenterX) == 3:
            CenterX = CenterX

        elif len(CenterX) == 2:
            CenterX = '0' + CenterX

        elif len(CenterX) == 1:
            CenterX = '00' + CenterX

        elif len(CenterX) == 0:
            CenterX = '000' + CenterX

#---------------------------------------------------------------------------

        if len(CenterY) == 3:
            CenterY = CenterY

        elif len(CenterY) == 2:
            CenterY = '0' + CenterY

        elif len(CenterY) == 1:
            CenterY = '00' + CenterY

        elif len(CenterY) == 0:
            CenterY = '000' + CenterY

#---------------------------------------------------------------------------

        ArduinoData = str(CenterX + CenterY)

#---------------------------------------------------------------------------

        currposData = ArduinoData

        if (currposData != prevposData):
            #print(ArduinoSerial.read())

            print(ArduinoData, CenterX, CenterY)
            ArduinoSerial.write(ArduinoData.encode('utf-8'))
            time.sleep(.1)

            prevposData = currposData

    cv2.imshow('Camera', frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()