
// Declare the input pin at 0
int analogPin = 0;


void setup() {
  // Begin the code 
  Serial.begin(9600);
}

// Main code that runs repeatedly
void loop() {
  // Read the raw data on analogPin
  float input = analogRead(analogPin);
  // Convert the raw data value (0 - 1023) to voltage (0.0V - 5.0V)
  double voltage = input * (5.0 / 1024.0);
  // Write the voltage value
  Serial.println(voltage, DEC);
  // Wait for 10sec, then repeat the code above.
  delay(10000);
}
