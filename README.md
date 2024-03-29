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
import time
import thingsboard

WIFI_AP = "StayHome"
WIFI_PASSWORD = "JustGuessIt"
TOKEN = "mrU9ltHmgtyCzmDMrjyP"
THINGSBOARD_SERVER = "tb.wouterpeetermans.com"
SERIAL_DEBUG_BAUD = 9600
echoPin1 = 2  # Echo Pin for sonar 1
trigPin1 = 14  # Trigger Pin for sonar 1
echoPin2 = 0  # Echo Pin for sonar 2
trigPin2 = 4  # Trigger Pin for sonar 2

tb = thingsboard.ThingsBoard(THINGSBOARD_SERVER, TOKEN)
dht = thingsboard.DHT11(5)

last_msg = 0
temperature = 0
humidity = 0
distance = 0
distance3 = 1  # om de count te doen kloppen
count = 0
free_slot = 0

def setup():
    thingsboard.serial_debug_begin(SERIAL_DEBUG_BAUD)
    dht.setup()

    setup_wifi()

def setup_wifi():
    thingsboard.delay(10)
    thingsboard.serial_println()
    thingsboard.serial_print("Connecting to ")
    thingsboard.serial_println(WIFI_AP)
    thingsboard.connect_wifi(WIFI_AP, WIFI_PASSWORD)
    while not thingsboard.is_wifi_connected():
        thingsboard.delay(500)
        thingsboard.serial_print(".")
    thingsboard.serial_println()
    thingsboard.serial_println("WiFi connected")
    thingsboard.serial_println("IP address: ")
    thingsboard.serial_println(thingsboard.get_local_ip())

def loop():
    global last_msg, temperature, humidity, distance, distance3, count, free_slot

    if not tb.connected():
        thingsboard.serial_print("Connecting to: ")
        thingsboard.serial_print(THINGSBOARD_SERVER)
        thingsboard.serial_print(" with token ")
        thingsboard.serial_println(TOKEN)
        if not tb.connect():
            thingsboard.serial_println("Failed to connect")
            return

    now = thingsboard.millis()
    if now - last_msg > 5000:
        last_msg = now
        thingsboard.serial_println("Sending data...")
        new_values = dht.get_temp_and_humidity()
        if dht.get_status() != 0:
            thingsboard.serial_println("DHT11 error status: " + dht.get_status_string())

        temperature = new_values.temperature
        temp_string = "{:.2f}".format(temperature)

        humidity = new_values.humidity
        hum_string = "{:.2f}".format(humidity)

        distance = get_distance_cm()
        dis_string = str(distance)

        distance1 = duration1 / 58
        distance1 = 1 if distance1 < 10 else 0

        distance2 = duration2 / 58

        # Update count and free_slot
        count = distance1 + distance2 + distance3
        free_slot = 3 - count

        thingsboard.serial_println(free_slot)

        tb.send_telemetry("temp", temperature)
        tb.send_telemetry("hum", humidity)
        tb.send_telemetry("slot", free_slot)

    tb.loop()

def get_distance_cm():
    duration = thingsboard.pulse_in(echoPin1, thingsboard.HIGH)
    return int(duration * 0.0343 / 2)

setup()
while True:
    loop()
    thingsboard.delay(10)

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



