import RPi.GPIO as GPIO
import time
import pygame

outPin = 4
repeat = 3

def alarm_mp3():
    pygame.mixer.init()
    pygame.mixer.music.load("./warning.mp3")
    pygame.mixer.music.play()

def alarm():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(outPin, GPIO.OUT)

    # Warm up alarm
    GPIO.output(outPin, 1)
    time.sleep(2)

    for x in range(0, repeat):
        GPIO.output(outPin, 0)
        time.sleep(0.5)
        GPIO.output(outPin, 1)
        time.sleep(2)

    GPIO.output(outPin, 0)

    GPIO.cleanup()

if __name__ == '__main__':
    # test1.py executed as script
    # do something
    alarm()
