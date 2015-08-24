import RPi.GPIO as GPIO
import time

led = 17
duration = 12

def light():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(led, GPIO.OUT)

    GPIO.output(led, 1)
    time.sleep(duration)

    GPIO.output(led, 0)
    GPIO.cleanup()

if __name__ == '__main__':
    # test1.py executed as script
    # do something
    light()