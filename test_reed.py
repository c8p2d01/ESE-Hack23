#! / usr / bin / python3
# Reed.py file
import time, sys
import RPi. GPIO as GPIO
GPIO.setmode (GPIO. BOARD)
GPIO setup (15, GPIO .IN, pull_up_down = GPIO.PUD_UP)
while True:
input = GPIO.input (15)
print (input)
time.sleep (1)