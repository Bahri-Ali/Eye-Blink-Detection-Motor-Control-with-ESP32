#include <Arduino.h>
#include <ESP32Servo.h>  

const int redLedPin = 23;
const int greenLedPin = 22;
const int servoPin = 17;
const int withLedPin = 5;

int po = 0;
int direction = 1;  
bool moveServo = false;

Servo myServo;

void setup() {
  Serial.begin(115200);      
  pinMode(redLedPin, OUTPUT);
  pinMode(greenLedPin, OUTPUT);
  pinMode(withLedPin, OUTPUT);
  myServo.attach(servoPin);  
}

void loop() {

  if (Serial.available() > 0) {       
    char val = Serial.read();          

    if (val == '0') {                   
      digitalWrite(redLedPin, HIGH);
      digitalWrite(greenLedPin, LOW);
      moveServo = false;   
    } 
    else if (val == '1') {             
      digitalWrite(redLedPin, LOW);
      digitalWrite(greenLedPin, HIGH);
      moveServo = true;    
    }
  }

  if (moveServo) {

    po += direction;        
    myServo.write(po);

    if (po >= 100) {
      direction = -1;
    }
    else if (po <= 0) {
      direction = 1;
    }

    delay(20);  
  }
}




