import pyautogui, sys
import time 
import serial

ArduinoSerial = serial.Serial('com3', 38400)  #Specify the correct COM port

prevposData = 00000000

while True:

   (x, y) = pyautogui.position()

   xpos = str(x)
   ypos = str(y)

#---------------------------------------------------------------------------

   if len(xpos) == 4:
      xpos = xpos

   elif len(xpos) == 3:
      xpos = '0' + xpos

   elif len(xpos) == 2:
      xpos = '00' + xpos

   elif len(xpos) == 1:
      xpos = '000' + xpos

   elif len(xpos) == 0:
      xpos = '0000' + xpos

#---------------------------------------------------------------------------

   if len(ypos) == 4:
      ypos = ypos

   elif len(ypos) == 3:
      ypos = '0' + ypos

   elif len(ypos) == 2:
      ypos = '00' + ypos

   elif len(ypos) == 1:
      ypos = '000' + ypos

   elif len(ypos) == 0:
      ypos = '0000' + ypos

#---------------------------------------------------------------------------

   posData = str(xpos + ypos)

   currposData = posData

   if (currposData != prevposData):
      #print(ArduinoSerial.read())

      print(posData.encode('utf-8'))
      ArduinoSerial.write(posData.encode('utf-8'))
      time.sleep(.3)

      prevposData = currposData