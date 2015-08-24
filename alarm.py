import RPi.GPIO as GPIO
import time

outPin = 4
interval = 1
repeat = 2

GPIO.setmode(GPIO.BCM)
GPIO.setup(outPin, GPIO.OUT)

# Warm up alarm
GPIO.output(outPin, 1)
time.sleep(2)

for x in range(0, repeat):
    GPIO.output(outPin, 0)
    time.sleep(interval)

    GPIO.output(outPin, 1)
    time.sleep(interval)

GPIO.output(outPin, 0)

GPIO.cleanup()
