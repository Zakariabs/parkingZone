# **ParkingⓏone**




### **Korte introductie**

Men probeert al van lang geleden  manieren te vinden om hedendaagse problemen op te lossen zoals: 
* Milieu vervuiling 
* Broeikaseffect 
* Geluidsoverlast
* etc.

Door goed na te denken kan men ideeën vinden die op hun buurt worden uitgewerkt en leiden tot een service die één of meerdere problemen kan oplossen. 


---

### Ons concept
#### Probleemstelling
In drukke metropolen is de populatie steeds aan het uitbreiden. Ongever 2 van de 3 individuen beschikken over een wagentje waarvan een aantal 2 tot 3 auto's hebben. Daarnaast worden de metropolen en de steden bezocht door pendelaars en bezoekers waardoor de parkeercapaciteiten in de metropolen en steden volzet geraken. 

Men blijft minuten opzoek naar een parkeerplaats. 


#### Oplossing: 
Door eerst een onderzoek te doen gaan we kijken waar in de metropolen te weinig parkeerplaatsten zijn. Daar gaan we onze gloednieuwe service aanbieden. Namelijk **ParkingⓏone**.ù

Een slimme parking box die geplaatst wordt in verschillende straten. Om de beschikbare parkeerplaatsen weer te geven aan de bestuurders.

![](https://i.imgur.com/wucbuMq.jpg)




---
--- 

###  **Onze werkplan**


ParkingZone is verschillende stappen ondergaan. Hieronder hebben we een overzicht gemaakt van destappenplan die we hebben gevolgd. 

---
### 1. **Brainstorming & Research**
Elke service behandelt een bestaande probleem. We zijn eerst begonnen met het behandelen van één van de meeste voorkomende problemen en dat is **Parkeren**.
![](https://i.imgur.com/50NZCly.png)

Eventuele mogelijke componenten en materiaal die we nodig hebben:
-  Ontwikkelbordje type ESP32
-  2 x SRF05 afstandsensor
-  10k ohm en 4.7k ohm weestandjes
-  Breadbord
-  Lege Cornflakes doosje
-  Zwarte teep 
-  Schaar 
-  Powerbank

---

### 2. **Design**
     
Nadat we een beeld kregen van de service die we willen aanbieden. Zijn  we  aan de slag gegaan om onze idee in kaart te brengen.
We hebben 2 ontwerpen gemaakt:
    
    
#### 1. **Data-ontwerp**
Deze ontwerp laat duidelijk zien hoe de data circuleert. vanaf het          moment dat de bestuurder pakeert op de site tot zijn vertrek.
         
 ![](https://i.imgur.com/E9zXhrr.png)

         
         
![](https://i.imgur.com/D4tLKoX.png)


#### 2. **Parking ontwerp**
Door parkeerruimtes te voorzien op straten en deze parkeerruimtes uit te rusten met een slimme Smart P-box. Deze zijn uitgerust met SRF05 en DHT11 sensors. 

- voorbeeld 1: Slimme Parkeerpalen
          
 ![](https://i.imgur.com/VfkdctI.jpg)

- Voorbeeld 2: Bovengronds
          
![](https://i.imgur.com/2cLztNl.png)
    

- Voorbeeld 3: Op de grond
![](https://i.imgur.com/0bd2FJM.jpg)

     
#### 3. **Schakel circuit**


Voor het aansluiten van de SRF05 sensor op de ESP32 hebben we het volgend schematje gebruikt. Rekeninghoudend met de spanningsdelers om de ESP32 niet kapot te krijgen. Daarnaast hebben we de keuze gehad om een DHT11 sensor toe te voegen aan de schakeling. Heel handig een idee te hebben over de weersituatie in de regio waarin de Smart P-Box zich bevindt. 


- Schema voor de afstandsensor: 
![](https://i.imgur.com/BAmnNVq.png)

- Schema voor de DHT11-sensor:
![](https://i.imgur.com/gnjxt5r.png)

---

#### 4. **Developement**

 De projectontwikkeling is verschillende stappen ondergaan. Vooaralleer we deze konden presenteren.

**Week 1:** Na een brainstorming wisten we aan wat we gaan beginnen.
We hebben een naam gekozen voor ons project. Een website voor de documentatie en de nodige materiaal bijeen gebracht zodat we aan onze smart P-Box kunnen beginnen, die we later gaan gebruiken in de parkeersites.

**Week 2:** Het project heeft een design nodig zodat we een visuele beeld hebben van ons project. Daarom hebben 3 Types designs proberen te verkijgen. Namelijk: 
 
- Parking Design: 
Het is belangrijk om een idee te hebben hoe de parking eruit gaat zien in de toekomst en de uitrusting daarvan. De bedoeling is dat we de Smart P-box bij elke parkeerplek gaan plaatsten. 
- Circuit Design: 
Om het ontwikkelbordje ESP32 met de sensoren te laten communiceren, moeten  deze juist geschakeld worden. Daarom zijn we opzoek gegaan naar handige informatie waarop we ons gaan baseren om de componenten juist met elkaar te kunnen schakelen. 
- Data Design: 
We willen dat de waardes die de Smart P-box meet, gelezen kunnen worden op ons dashbord. Zodat we achteraf de beschikbaarheid van vrije parkeerplaastsen kunnen weergeven aan de klant.
Om dat waar te maken, maken we gebruik van een iot platform, namelijk Thingsboard. Achteraf waren we genoodzaakt om gebruik te maken van de Microsoft Azure iot platform omdat we gebruik moesten maken van gesimuleerde data. 

**Week 3 t/m 5:** 

Nu is het tijd om het ontwikkelbordje te schakelen met de SRF05 en DHT11 sensors. Door gebruik te maken van een printplaat zijn we zekerder van de stabiliteit van de schakeling. Maar wegens de omstandigheden moesten we het verder doen met een breadbordje. 
Nadat we de ic-schakeling hebben afgerond volgens de gemaakte schema's was het tijd om aan de volgende stap te beginnen.

Om de ESP32 te laten communiceren met de sensoren hebben een werkende script nodig. Deze heeft de meeste tijd genomen omdat het ontwikkelbordje deels kapot was, ondervonden een probleem met de compoort van de ESP32. 
De code konden we niet uploaden. Na veel te surfen op het internet om erachter te komen wat de reden van de "ESPTOOL ERROR" is. zo te zien werkt de seriele poort  niet zo goed.

Dus hebben we besloten om een nieuwe bordje te bestellen. De troubleshooting + wachtijd van het nieuw bordje heeft zo'n 10 waardevolle dagen gekost. Toen het bordje is aan gekomen zijn we meteen terug aan de slag. Het is ons gelukt om de waardes te beginnen aflezen. 
We moesten nog ervoor zorgen dat enkel de beschikbare parkeerslots met de juiste temperatuur en vochtigehidswaarde verzonden worden naar de thingsboard server. maar helaas is de esp32 weer stuk gegaan een week voor de presentatie waardoor het niet meer mogelijk was om een nieuwe ontwikkelbordje tijdig te laten komen,toch hebben we het anders opgelost. 

Enkele weken geleden was ik aan het experimenteren met Microsoft Azure Iot.
Deze geeft de mogelijkheid om sensoren te simuleren. Deze data kon ik weergeven op een dashbord. Zo hebben ons dahsbord tijdig afegekregen voor de presentatie.

Uiteindelijk hebben we de Smart P-box kunnen monteren in de volgende stappen:

####  - Monteren van de IC-Schakeling:                                                  
Materiaal bijeen brengen en juiste schakelen volgens de schema's. 
 
![](https://i.imgur.com/6qOOpx5.jpg)

#### - Plaatsen van de IC-Schakeling in de lege box
![](https://i.imgur.com/dZaJlrJ.jpg)

- Smart P-box is klaar! 
![](https://i.imgur.com/sXSzKjc.jpg)

#### - Dashbord is klaargezet

![](https://i.imgur.com/GqclaBN.png)

#### Hierboven wordende volgende  zaken weergeven:
*  Beschikbaarheid van de parkeerplaasten. Indien beschibaar true, anders false.
* Ovezicht van de beschibare parkeerplaatsen. 
* Temperatuur, vochtigheid en druk. 
* Batterijniveau 
* Aantal reservingen van de parkeerplaasten.
* Locatie van de parkeerslot


#
**Hieronder is de gebruikte arduino script te vinden:**
```
// This sketch demonstrates connecting and sending telemetry
// using ThingsBoard SDK
//
// Hardware:
//  - Arduino Uno
//  - ESP8266 connected to Arduino Uno
#include "ThingsBoard.h"
#include <WiFi.h>
#include "DHTesp.h"
#define WIFI_AP             "StayHome"
#define WIFI_PASSWORD       "JustGuessIt"


// See https://thingsboard.io/docs/getting-started-guides/helloworld/
// to understand how to obtain an access token


#define TOKEN               "mrU9ltHmgtyCzmDMrjyP"
#define THINGSBOARD_SERVER  "tb.wouterpeetermans.com"


// Baud rate for serial debug
#define SERIAL_DEBUG_BAUD   9600


#define echoPin1 2 // Echo Pin for sonar 1
#define trigPin1 14 // Trigger Pin for sonar 1

#define echoPin2 0 // Echo Pin for sonar 1
#define trigPin2 4 // Trigger Pin for sonar 1
long duration1, distance1; 
long duration2, distance2; 
long duration3, distance3; 
// Initialize the WiFI client object
WiFiClient espClient;

// Initialize ThingsBoard instance
ThingsBoard tb(espClient);


DHTesp dht;


long lastMsg = 0;
char msg[50];
int value = 0;

const unsigned int TRIG_PIN = 0;
const unsigned int ECHO_PIN = 4;

float temperature = 0;
float humidity = 0;
float distance = 0;
int distance3 = 1 // om de count te doen kloppen
int count = 0;
int freeSlot = 0;
void setup() {
  // initialize serial for debugging
  Serial.begin(SERIAL_DEBUG_BAUD);
  dht.setup(5, DHTesp::DHT11);
  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);
  setup_wifi();
}


void setup_wifi() {

  delay(10);
  // We start by connecting to a WiFi network
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(WIFI_AP);
  WiFi.begin(WIFI_AP, WIFI_PASSWORD);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
}


void loop() {

  if (!tb.connected()) {
    // Connect to the ThingsBoard
    Serial.print("Connecting to: ");
    Serial.print(THINGSBOARD_SERVER);
    Serial.print(" with token ");
    Serial.println(TOKEN);
    if (!tb.connect(THINGSBOARD_SERVER, TOKEN)) {
      Serial.println("Failed to connect");
      return;
    }
  }
  long now = millis();
  if (now - lastMsg > 5000) {
    lastMsg = now;
    Serial.println("Sending data...");
    TempAndHumidity newValues = dht.getTempAndHumidity();
    if (dht.getStatus() != 0) {
      Serial.println("DHT11 error status: " + String(dht.getStatusString()));
    }

    // Temperature in Celsius
    temperature = newValues.temperature;
    // Uncomment the next line to set temperature in Fahrenheit
    // (and comment the previous temperature line)
    //temperature = 1.8 * bme.readTemperature() + 32; // Temperature in Fahrenheit

    // Convert the value to a char array
    String tempString;
    tempString = String(temperature);
    Serial.print("Temperature: ");
    Serial.println(tempString);
    humidity = newValues.humidity;

    // Convert the value to a char array
    String humString;
    humString = String(humidity);
    Serial.print("Humidity: ");
    Serial.println(humString);
    int distance = getDistanceCm();

    String disString;
    disString = String(distance);
    Serial.print("Distance: ");
    Serial.println(disString);
    const unsigned long duration = pulseIn(ECHO_PIN, HIGH);


    distance1 = duration1 / 58.2;
    if (distance1 < 10)
      distance1 = 1;
    else distance1 = 0;

     distance2 = duration2 / 58.2;
    if (distance2 < 10)
      distance2 = 1;
    else distance1 = 0;

    count = distance1 + distance2 + distance3;
    freeSlot = 3 - count;
    // number of total slot is sent to esp32
    Serial.println(freeSlot);
    // the status is updated every 30 seconds.
    delay(5000);


    
    tb.sendTelemetryFloat("temp", temperature);
    tb.sendTelemetryFloat("hum", humidity);
    tb.sendTelemetryFloat("slot", freeSlot);
  }

  tb.loop();
}
int getDistanceCm() { //een functie die de meting uitvoert en de afstand returned.
  long duration;
  // Clears the trigPin
  digitalWrite(TRIG_PIN, LOW);
  delayMicroseconds(2);
  // Sets the trigPin on HIGH state for 10 micro seconds
  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN, LOW);
  // Reads the echoPin, returns the sound wave travel time in microseconds
  duration = pulseIn(ECHO_PIN, HIGH); //pulseIn meet de tijd dat het duurt voor deze pin terug hoog wordt.
  // Calculating the distance
  return duration * 0.0343 / 2;
}
```

 
---
5. #### Test & Evaluation


We kunnen zeggen dat onze project deels gelukt is. 
De bedoeling was om een prototype van de Smart P-box af te ronden met de juiste schakeling en vorm. 
Daarnaast is het gelukt om een Dashbord te maken met gesimuleerde data. 
Er waren veel tegenslagen, stress momenten en teleurstelling omdat we geen echte data hebben kunnen verkrijgen, ontwikkelbordjes gingen kapot enzovoort. Maar we hebben niet opgegeven! 

Het project stopt hier niet. De bedoeling is dat we daaraan verder gaan werken tot we ons doel bereikt hebben.

We hebben veel uit dit project en veel fouten ontdekt. Te laat beginnen was het voornaamste fout. Daardoor zijn we veel tijd verloren en de speling die we konden hebben om zaken die mislopen zoals  "de esp32" tijdig op te lossen en op tijd het project af te ronden. Uiteindelijk leren we van onze fouten.

We zijn toch wel blij met wat we hebben bereikt, maar het kon toch wel beter gaan.



---
6. #### Presentation

De laaste 3 dagen hebben we gebruikt om een leuke presentatie te maken. 
We kozen voor Prezi om onze presentatie zo interactief mogelijk te maken.
De DD-Day is aangebroken en het werd tijd om te presenteren. Na een adempje te nemen en wat stressgevoel hebben we ons project in beeld gebracht! 

>                         Een laatste woordje µ
>                Bij deze komt deze documentaie tot einde. Bedankt om te lezen !        



