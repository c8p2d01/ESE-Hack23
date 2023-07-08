#Hackathon 2023
import RPi.GPIO as GPIO
import time
from gpiozero import LED #Fuer Steuerung der Lampen

#Pin Belegung
#Reed
reed_links_aussen_pin = 11
reed_links_innen_pin = 23
reed_rechts_innen_pin = 24
reed_rechts_aussen_pin = 25

class bahn_sensor
	def __init__(self)
		self.status_innen = 0
		self.activation_innen = time.time()
		self.status_aussen = 0
		self.activation_aussen = time.time()

	def checkTravel(self):
		currTime = time.time()
		if (self.status_aussen == 1 && self.status_innen == 1):
			if (self.activation_aussen > self.activation_innen):
				schliesse_Uebergang()
			else:
				oeffneUebergang()
	
	def activate_aussen(self):
		self.status_aussen = 1
		self.activate_aussen = time.time()
		self.checkTravel()
	
	def activate_innen(self):
		self.status_innen = 1
		self.activate_innen = time.time()
		self.checkTravel()

bahnSensorLinks = bahn_sensor()

# Led Strasse
strassen_leds = LED(20)
#Led Zug
bahn_led_links = LED(4)
bahn_led_rechts = LED(16)

#Servo

GPIO.setmode(GPIO.BCM)
GPIO.setup(reed_links_aussen_pin, GPIO.IN)
GPIO.setup(reed_links_innen_pin, GPIO.IN)
GPIO.setup(reed_rechts_innen_pin, GPIO.IN)
GPIO.setup(reed_rechts_aussen_pin, GPIO.IN)

reed_status

def activate_links_aussen(reed_links_aussen_pin):
	bahnSensorLinks.activate_aussen()
def callback_function2(reed_links_innen_pin):
	print("links innen")
def callback_function3(reed_rechts_innen_pin):
	print("rechts innen")
def callback_function4(reed_rechts_aussen_pin):
	print("rechts aussen")

GPIO.add_event_detect(reed_links_aussen_pin, GPIO.FALLING, callback=callback_function1, bouncetime=200)
GPIO.add_event_detect(reed_links_innen_pin, GPIO.FALLING, callback=callback_function2, bouncetime=200)
GPIO.add_event_detect(reed_rechts_innen_pin, GPIO.FALLING, callback=callback_function3, bouncetime=200)
GPIO.add_event_detect(reed_rechts_aussen_pin, GPIO.FALLING, callback=callback_function4, bouncetime=200)

#Bahnuebergang sichern
# Straßen-LED einschalten
strassen_leds.on()

#wenn der Bahnübergang gesichert ist, dann die richtige Richtung mit Blinklicht freigeben

if richtung == links:
# Bahn-LED im Verhältnis 1 Sekunde zu 1 Sekunden blinken lassen
bahn_led_links.blink(1,1)
elif richtung == rechts:
# Bahn-LED im Verhältnis 1 Sekunde zu 1 Sekunden blinken lassen
bahn_led_rechts.blink(1,1)

# Signal geben wenn der Bahnübergang frei ist

#Bahnuebergang freischalten, wenn der Bahnuebergang frei ist
# Straßen-LED ausschalten
strassen_leds.off()
# Bahn-LEDs ausschalten
bahn_led_rechts.off()
bahn_led_links.off()

