import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

led = 4

GPIO.setup(led, GPIO.OUT)

GPIO.output(led, 1)
time.sleep(5)

GPIO.output(led, 0)

GPIO.cleanup()
