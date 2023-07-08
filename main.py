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

# Led Strasse
strassen_leds = LED(20)

def bahnlicht_freigabe(seite):
	print("\e[38;5;196mBahn kann kommen\n\e[0m")
	if (seite == "links"):
		bahn_led_links.blink(1, 1)
	else:
		bahn_led_rechts.blink(1, 1)

def bahnlicht_ende(seite):
	print("\e[38;5;42mBahn ist durch\n\e[0m")
	bahn_led_links.off()
	bahn_led_rechts.off()

class Schranke():
  def __init__(self,pinMotor,pinKontakt):
    self.open = False
    self.pinMotor = pinMotor
    self.pinKontakt = pinKontakt
    GPIO.setup(pinMotor, GPIO.OUT)

  def open(self):
    p = GPIO.PWM(self.pinMotor, 50)  # GPIO 17 als PWM mit 50Hz
    p.start(0)
    p.ChangeDutyCycle(7.5)
  def close(self):
    p = GPIO.PWM(self.pinMotor, 50)  # GPIO 17 als PWM mit 50Hz
    p.start(0)
    p.ChangeDutyCycle(0)
  def check(self):
    pass

class bahn_sensor:
	def __init__(self,seite):
		self.status_innen = 0
		self.activation_innen = time.time()
		self.status_aussen = 0
		self.activation_aussen = time.time()
		self.name = seite

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
	
	def activate_aussen(self):
		self.status_aussen = 1
		self.activate_aussen = time.time()
		self.checkTravel()
	
	def activate_innen(self):
		self.status_innen = 1
		self.activate_innen = time.time()
		self.checkTravel()

bahnSensorLinks = bahn_sensor("links")
bahnSensorRechts = bahn_sensor("rechts")

# False -> kein Zug im Bahnübergang, True -> Bahn im Zugübergang
innen:bool = False
aussen:bool = False

def	strassenlicht_switch():
	global aussen
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

def	Fehlerzustand():
	strassen_leds.on
	bahn_led_links.off()
	bahn_led_rechts.off()
	#Schranken zu?

#Servo

GPIO.setmode(GPIO.BCM)
GPIO.setup(reed_links_aussen_pin, GPIO.IN)
GPIO.setup(reed_links_innen_pin, GPIO.IN)
GPIO.setup(reed_rechts_innen_pin, GPIO.IN)
GPIO.setup(reed_rechts_aussen_pin, GPIO.IN)

def callback_function1():
	print("reed lonks aussen\n")
	bahnSensorLinks.activate_aussen()
	strassenlicht_switch()
def callback_function2():
	bahnSensorLinks.activate_innen()
	strassenschranken_switch()
def callback_function3():
	bahnSensorRechts.activate_aussen()
	strassenlicht_switch()
def callback_function4():
	bahnSensorRechts.activate_innen()
	strassenschranken_switch()

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

