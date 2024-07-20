#include <Servo.h>

Servo servo1;
Servo servo2;

const byte numValues = 2; // number of values in the array
int values[numValues]; // initialize array to hold received values
byte i = 0; // counter for the array index
int val_1,val_2,val_3,val_4;


void setup() {
  Serial.begin(9600); // initialize serial communication
  servo1.attach(9);
  servo2.attach(11);
}

void loop() {
  if (Serial.available() > 0) { // check if data is available
    String data = Serial.readStringUntil('\n'); // read the data as string
    int start = 0; // start index for extracting numbers from string
    for (byte end = 0; end < data.length(); end++) { // loop through the string
      if (data.charAt(end) == ',') { // check for comma delimiter
        values[i] = data.substring(start, end).toInt(); // extract and convert the number
        i++; // increment the array index
        start = end + 1; // update the start index
      }
    }
    values[i] = data.substring(start, data.length() - 1).toInt(); // extract the last number
    i = 0; // reset the array index
    // do something with the received values
    
  }
    val_1 = values[0]; 
    val_2 = values[1];

    servo1.write(val_1);
    servo2.write(val_2);
      Serial.println(values[0]);
      Serial.println(values[1]);

}
