#Hackathon 2023
import RPi.GPIO as GPIO
from gpiozero import LED #Fuer Steuerung der Lampen


#Pin Belegung
#Reed
reed_links_aussen_pin = 11
reed_links_innen_pin = 23
reed_rechts_innen_pin = 24
reed_rechts_aussen_pin = 25

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

def callback_function(reed_links_aussen_pin):
	print("Zug")
def callback_function(reed_links_innen_pin):
	print("Zug")
def callback_function(reed_rechts_innen_pin):
	print("Zug")
def callback_function(reed_rechts_aussen_pin):
	print("Zug")

GPIO.add_event_detect(reed_links_aussen_pin, GPIO.FALLING, callback=callback_function, bouncetime=200)
GPIO.add_event_detect(reed_links_innen_pin, GPIO.FALLING, callback=callback_function, bouncetime=200)
GPIO.add_event_detect(reed_rechts_innen_pin, GPIO.FALLING, callback=callback_function, bouncetime=200)
GPIO.add_event_detect(reed_rechts_aussen_pin, GPIO.FALLING, callback=callback_function, bouncetime=200)

#Bahnuebergang sichern
# Straßen-LED einschalten
strassen_leds.on()

#wenn der Bahnübergang gesichert ist, dann die richtige Richtung mit Blinklicht freigeben
richtung = getDirection()

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

class bahn_detection
	def __init__(self, reed_innen, reed_aussen)
		self.name = 
