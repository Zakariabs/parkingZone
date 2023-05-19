import time
import thingsboard

WIFI_AP = "StayHome"
WIFI_PASSWORD = "JustGuessIt"
TOKEN = "YOUR TOKEN"
THINGSBOARD_SERVER = "Your_SERVER.com"
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
