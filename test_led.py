# This is a sample Python script.
import RPi.GPIO as GPIO
import time


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def test():
    # Use a breakpoint in the code line below to debug your script.

    led = 4

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(led, GPIO.OUT)

    try:
        while True:
            GPIO.output(led, 1)  # 1/0, True/False, GPIO.HIGH/GPIO.LOW accepted
            time.sleep(5)  # 5 seconds light on
            GPIO.output(led, False)
            time.sleep(5)  # 5 seconds light off

    except KeyboardInterrupt:
        print("Quit")
        GPIO.output(led, GPIO.LOW)
        GPIO.cleanup()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
