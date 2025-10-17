#include <Servo.h>
int servoPos = 40;  // 30 to 46
int servoPin = 9;
String cmd;
Servo grabAxis;

void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
grabAxis.attach(servoPin);
}

void loop() {
  // put your main code here, to run repeatedly:
while(Serial.available()==0){
  
  }
cmd = Serial.readStringUntil('\r');
if (cmd == "buka"){
  grabAxis.write(30);
  }
else {
  grabAxis.write(46);
  }
}
