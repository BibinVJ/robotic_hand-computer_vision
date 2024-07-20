#include<Servo.h>
#include<EEPROM.h>

Servo wrist;
Servo elbow;
Servo gripper;
Servo base;
Servo arm;

int pin1=A0;
int pin2=A1;
int pin3=A2;
int pin4=A3;
int pin5=A4;
int val;
int data;

void setup() {
  //setting the servo pins
  pinMode(pin1,INPUT);
  pinMode(pin2,INPUT);
  pinMode(pin3,INPUT);
  pinMode(pin4,INPUT);
  pinMode(pin5,INPUT);
  wrist.attach(3);
  elbow.attach(4);
  gripper.attach(5);
  base.attach(6);
  arm.attach(7);

}

void loop() {
  // controlling the servo based on the pot signal
  val = analogRead(pin1);
  val=map(val,0,1023,0,180);
  EEPROM.write(data,val);
  wrist.write(val);
  delay(1);
  
  val = analogRead(pin2);
  val=map(val,0,1023,0,180);
  EEPROM.write(data,val);
  elbow.write(val);
  delay(1);
  
  val = analogRead(pin3);
  val=map(val,0,1023,0,180);
  EEPROM.write(data,val);
  gripper.write(val);
  delay(1);
  
  val = analogRead(pin4);
  val=map(val,0,1023,0,180);
  EEPROM.write(data,val);
  base.write(val);
  delay(1);

  val = analogRead(pin5);
  val=map(val,0,1023,0,180);
  EEPROM.write(data,val);
  arm.write(val);
  delay(1);

}
