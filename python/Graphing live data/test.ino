
// Said Gourida

int led = 6;
int pinecho = 10;
int pintrig = 9;
long Time;



void setup() {
  Serial.begin(1200);
  pinMode(led, OUTPUT);
  pinMode(pinecho, INPUT);
  pinMode(pintrig, OUTPUT);
}
void loop() {
  digitalWrite(pintrig, HIGH);
  delay(1000);
  digitalWrite(pintrig, LOW);
  Time = pulseIn(pinecho, HIGH);
  Time = (Time / 2) / 29.1;
  Serial.print(Time);
  Serial.println("cm");
  delay(10);

  if ((Time <= 10))
  {
    digitalWrite(led, HIGH);
  }
  else if (Time > 10)
  {
    digitalWrite(led, LOW);
  }
}
