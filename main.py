#Hackathon 2023
import RPi.GPIO as GPIO
import time
from gpiozero import LED #Fuer Steuerung der Lampen

#Makros
# sensor_timeout = 3000.0

#Pin Belegung
#Reed
reed_links_aussen_pin = 11
reed_links_innen_pin = 23
reed_rechts_innen_pin = 24
reed_rechts_aussen_pin = 25

#Led Zug
bahn_led_links = LED(4)
bahn_led_rechts = LED(16)

#Schranken
schranke_vorne = 12
schranke_hinten = 27
schranke_hinten_offen = 26
schranke_vorne_offen = 11

# Led Strasse
strassen_leds = LED(20)

def bahnlicht_freigabe(seite):
    print("Bahn kann kommen\n")
    if (seite == "links"):
        bahn_led_links.blink(1, 1)
    else:
        bahn_led_rechts.blink(1, 1)

def bahnlicht_ende(seite):
    print("Bahn ist durch\n")
    bahn_led_links.off()
    bahn_led_rechts.off()

class Schranke():
    def __init__(self, pinMotor, pinKontakt):
        self.isOpen = False
        self.pinMotor = pinMotor
        self.pinKontakt = pinKontakt
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pinKontakt, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
        GPIO.setup(self.pinMotor, GPIO.OUT)


        self.p = GPIO.PWM(self.pinMotor, 50)
        self.p.start(3.75)

    def open(self):
         # GPIO 17 als PWM mit 50Hz

        self.p.ChangeDutyCycle(3.75)

    def close(self): # GPIO 17 als PWM mit 50Hz

        self.p.ChangeDutyCycle(7.5)

    def check(self):
        if GPIO.input(self.pinKontakt) == GPIO.HIGH:
            self.isOpen = True
        else:
            self.isOpen = False
        return self.isOpen

class bahn_sensor:
    def __init__(self,seite):
        self.status_innen = 0
        self.activation_innen = time.time()
        self.status_aussen = 0
        self.activation_aussen = time.time()
        self.name = seite

    def reset(self):
        self.status_aussen = 0
        self.status_innen = 0

    def checkTravel(self):
        # currTime = time.time()
        # if (self.activation_aussen + sensor_timeout > currTime):
        # 	self.status_aussen = 0
        # if (self.activation_innen + sensor_timeout > currTime):
        # 	self.status_innen = 0
        if (self.status_aussen == 1 and self.status_innen == 1):
            if (self.activation_aussen > self.activation_innen):
                bahnlicht_freigabe(self.name)
            else:
                bahnlicht_ende(self.name)
            self.reset()

    def activate_aussen(self):
        self.status_aussen = 1
        self.activate_aussen = time.time()
        self.checkTravel()

    def activate_innen(self):
        self.status_innen = 1
        self.activate_innen = time.time()
        self.checkTravel()
#Initialisierung
bahnSensorLinks = bahn_sensor("links")
bahnSensorRechts = bahn_sensor("rechts")
SchrankeV = Schranke(schranke_vorne,schranke_vorne_offen)
SchrankeH = Schranke(schranke_hinten,schranke_hinten_offen)


# False -> kein Zug im Bahnübergang, True -> Bahn im Zugübergang
innen:bool = False
aussen:bool = False

def	strassenlicht_switch():
    global aussen
    print("		Licht switched\n")
    if (aussen):
        strassen_leds.off()
        aussen = False
    else:
        strassen_leds.on()
        aussen = True

def	strassenschranken_switch():
    global innen
    if (innen):
        #schranke auf
        innen = False
    else:
        #schranke zu
        innen = True

def	startup():
    strassen_leds.on()
    bahn_led_links.blink(1,1)
    bahn_led_rechts.blink(1,1)
    time.sleep(3)
    strassen_leds.off()
    bahn_led_links.off()
    bahn_led_rechts.off()
    SchrankeV.close()
    SchrankeH.close()
    print(SchrankeH.check())
    print(SchrankeV.check())
    SchrankeH.open()
    SchrankeV.open()



def	Fehlerzustand():
    strassen_leds.on()
    bahn_led_links.off()
    bahn_led_rechts.off()
    #Schranken zu?



GPIO.setmode(GPIO.BCM)
GPIO.setup(reed_links_aussen_pin, GPIO.IN)
GPIO.setup(reed_links_innen_pin, GPIO.IN)
GPIO.setup(reed_rechts_innen_pin, GPIO.IN)
GPIO.setup(reed_rechts_aussen_pin, GPIO.IN)

def callback_function1(t1):
    print("reed links aussen\n")
    bahnSensorLinks.activate_aussen()
    strassenlicht_switch()
def callback_function2(t1):
    print("reed links innen\n")
    bahnSensorLinks.activate_innen()
    # strassenschranken_switch()
def callback_function3(t1):
    print("reed rechts aussen\n")
    bahnSensorRechts.activate_aussen()
    strassenlicht_switch()
def callback_function4(t1):
    print("reed rechts innen\n")
    bahnSensorRechts.activate_innen()
    # strassenschranken_switch()

GPIO.add_event_detect(reed_links_aussen_pin, GPIO.FALLING, callback=callback_function1, bouncetime=200)
GPIO.add_event_detect(reed_links_innen_pin, GPIO.FALLING, callback=callback_function2, bouncetime=200)
GPIO.add_event_detect(reed_rechts_innen_pin, GPIO.FALLING, callback=callback_function3, bouncetime=200)
GPIO.add_event_detect(reed_rechts_aussen_pin, GPIO.FALLING, callback=callback_function4, bouncetime=200)

#Bahnuebergang sichern
# Straßen-LED einschalten

#wenn der Bahnübergang gesichert ist, dann die richtige Richtung mit Blinklicht freigeben

# #if richtung == links:
# # Bahn-LED im Verhältnis 1 Sekunde zu 1 Sekunden blinken lassen
# bahn_led_links.blink(1,1)
# elif richtung == rechts:
# # Bahn-LED im Verhältnis 1 Sekunde zu 1 Sekunden blinken lassen
# bahn_led_rechts.blink(1,1)

# Signal geben wenn der Bahnübergang frei ist

# #Bahnuebergang freischalten, wenn der Bahnuebergang frei ist
# # Straßen-LED ausschalten
# strassen_leds.off()
# # Bahn-LEDs ausschalten
# bahn_led_rechts.off()
# bahn_led_links.off()

startup()

while True:
    pass