#include<Servo.h>

Servo serX;
Servo serY;

String serialData;

int initialstate = 15;

void setup() {
    serX.attach(9);
    serY.attach(10);

    serX.write(initialstate);
    serY.write(initialstate);
    
    Serial.begin(9600);
    Serial.setTimeout(10);
}

void loop()  {
        //XD
}

void serialEvent() {
    serialData = Serial.readString();

    Serial.print(parseDataX(serialData));
    Serial.print("    ");
    Serial.println(parseDataY(serialData));

    servoWrite();

}

int parseDataX(String data) {
    data.remove(data.indexOf("Y"));
    data.remove(data.indexOf("X"), 1);

    return data.toInt();
}


int parseDataY(String data){
    data.remove(0, data.indexOf("Y") + 1);

    return data.toInt();
    
}

void servoWrite() {
  int servopos1 = parseDataX(serialData);
  int servopos2 = parseDataY(serialData);

  int servomappos1 = map(servopos1, 0, 1919, 15, 165);
  int servomappos2 = map(servopos2, 0, 1079, 15, 165);

  serX.write(servomappos1);
  serY.write(servomappos2);
}