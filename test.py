import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

led = 4
GPIO.setup(led, GPIO.OUT, initial=GPIO.LOW)
GPIO.output(led, True)

time.sleep(5)

GPIO.output(led, False)

GPIO.cleanup()
