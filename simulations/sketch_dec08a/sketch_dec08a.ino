int x=0,y=0,z=0;
void setup() {
  // put your setup code here, to run once:
  pinMode(A0,INPUT);
  pinMode(A1,INPUT);
  pinMode(A2,INPUT);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  x=analogRead(A0);
  y=analogRead(A1);
  z=analogRead(A2);
  Serial.println(TYPE_NAME(x));
  Serial.println((String)  "x="  +x+  ", y="   +y+   ", z="   +z);
  Serial.println(TYPE_NAME(x));
  delay(100000);
}
