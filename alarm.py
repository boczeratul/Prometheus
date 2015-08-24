import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

led = 4
interval = 1

GPIO.setup(led, GPIO.OUT)

GPIO.output(led, 1)
time.sleep(interval)

GPIO.output(led, 0)
time.sleep(interval)

GPIO.output(led, 1)
time.sleep(interval)

GPIO.output(led, 0)
time.sleep(interval)

GPIO.cleanup()
