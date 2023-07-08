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

#Bahnuebergang freischalten, wenn der Bahnuebergang frei ist
# Straßen-LED ausschalten
strassen_leds.off()
# Bahn-LEDs ausschalten
bahn_led_rechts.off()
bahn_led_links.off()

class 
