#include <dht.h>
#include <SPI.h>

dht DHT;

#define DHT11_PIN 7
#define SENSOR_PIN A0    // select the input pin for the potentiometer
#define LED_PIN 13       // select the pin for the LED

int sensorValue = 0;        // variable to store the value coming from the sensor

void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
  // declare the ledPin as an OUTPUT:
  pinMode(LED_PIN, OUTPUT);
}

void loop() {
  // read the value from the sensor:
  sensorValue = analogRead(SENSOR_PIN);

  // print out the state of the DHT11 sensor
  int chk = DHT.read11(DHT11_PIN);
  Serial.print("TEMP:");
  Serial.println(DHT.temperature);
  Serial.print("HUMI:");
  Serial.println(DHT.humidity);
  
  // print out the state of the analog sensor:
  Serial.print("MOIS:");
  Serial.println(sensorValue);

  // wait 2 second in between readings
  delay(2000);        
}
