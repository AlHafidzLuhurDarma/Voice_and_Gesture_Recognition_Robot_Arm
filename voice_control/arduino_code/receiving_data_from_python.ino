#include <Servo.h>

String cmd;

// X
int xPos;  //50 to 130
int xPin = 9;
// Y
int yPos = 70; //20 to 110
int yPin = 10;
// Z
int zPos = 40; // 20 to 60
int zPin = 11;

// Grab
int grabPos = 40; // 30 to 46
int grabPin = 6;


Servo xAxis, yAxis, zAxis, grabAxis;

void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
xAxis.attach(xPin);
yAxis.attach(yPin);
zAxis.attach(zPin);
grabAxis.attach(grabPin);
}

void loop() {
  // put your main code here, to run repeatedly:
while (Serial.available()==0){
  
  }
cmd = Serial.readStringUntil('\r');
if (cmd == "kanan"){
  xAxis.write(50);
  }
if (cmd == "kiri"){
  xAxis.write(130);
  }
if (cmd == "atas"){
  yAxis.write(20);
  }
if (cmd == "bawah"){
  yAxis.write(90);
  }
if (cmd == "maju"){
  zAxis.write(20);
  }
if (cmd == "mundur"){
  zAxis.write(60);
  }
if (cmd == "buka"){
  grabAxis.write(30);
  }
if (cmd == "tutup"){
  grabAxis.write(46);
  }
Serial.println(cmd);
}

// give 1 SG90S and 1 SG90 Servo an external power supply
// and 1 SG90S arduino power supply
// connect the gnd of the arduino into the breadboard that connected in to the external power supply
