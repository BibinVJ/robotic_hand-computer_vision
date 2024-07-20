const byte numValues = 2; // number of values in the array
int values[numValues]; // initialize array to hold received values
byte i = 0; // counter for the array index

void setup() {
  Serial.begin(9600); // initialize serial communication
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
      Serial.println(values[0]);

}
