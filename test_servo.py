import RPi.GPIO as GPIO
import time

servoPIN = 12



class Schranke():
    def __init__(self, pinMotor, pinKontakt):
        self.isOpen = False
        self.pinMotor = pinMotor
        self.pinKontakt = pinKontakt
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pinMotor, GPIO.OUT)
        #GPIO.setup(self.pinKontakt, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

        self.p = GPIO.PWM(self.pinMotor, 50)
        self.p.start(3.75)

    def open(self):
         # GPIO 17 als PWM mit 50Hz

        self.p.ChangeDutyCycle(3.75)

    def close(self): # GPIO 17 als PWM mit 50Hz

        self.p.ChangeDutyCycle(7.5)

    def check(self):
        #if GPIO.
        pass

if __name__ == '__main__':
    s = Schranke(servoPIN,12)
    try:
        while True:
            s.open()
            time.sleep(5)
            s.close()
            time.sleep(5)


    except KeyboardInterrupt:
        s.stop()
        GPIO.cleanup()