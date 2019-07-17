#include <DHT.h>
#define DHTPIN 9
#define DHTTYPE DHT11
DHT dht(DHTPIN, DHTTYPE);
void setup(){
  Serial.begin(9600);
  dht.begin();
}
void loop(){
  int h = dht.readHumidity()*10;
  int t = dht.readTemperature()*10;
  Serial.print(h);
  Serial.print(" ");
  Serial.println(t);
  delay(500);
    
}
