# This is a sample Python script.
import RPi.GPIO as GPIO
import time


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def test():
    # Use a breakpoint in the code line below to debug your script.

    led = 22

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(led, GPIO.IN)

    def callback_function(led):
        print("Zug")

    GPIO.add_event_detect(led, GPIO.FALLING, callback=callback_function, bouncetime=200)

    while True:
        print("Busy")
        time.sleep(3)
        print("Really busy")
        time.sleep(3)
        print("Still busy")
        time.sleep(3)



    GPIO.cleanup()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
