#include <cvzone.h>
#include <Servo.h>

Servo servo1;
Servo servo2;
SerialData serialData(2, 4); //(numOfValsRec,digitsPerValRec)
int valsRec[3]; // array of int with size numOfValsRec 
int val_1,val_2,val_3,val_4;
void setup() {
  //pinMode(13, OUTPUT);
  Serial.begin(9600);
  serialData.begin();
  servo1.attach(9);
  servo2.attach(11);
}

void loop() {

  serialData.Get(valsRec);
  val_1 = valsRec[0]; 
  val_2 = valsRec[1];
//  val_3 = valsRec[2];
//  val_4 = valsRec[3];
  
  Serial.println(val_1);
  Serial.println(val_2);
//  Serial.println(val_3);
//  Serial.println(val_4);

  servo1.write(val_1);
  servo2.write(val_2);
  
//  if (val == 0){
//    myservo.write(180);
//  }
//  if (val ==1){
//    myservo.write(0);
//  }
  delay(1000);
}
