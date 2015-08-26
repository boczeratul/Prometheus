import RPi.GPIO as GPIO
import time
import pygame

led_left = 17
led_right = 4

def start_speak():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(led_left, GPIO.OUT)
    GPIO.setup(led_right, GPIO.OUT)

    GPIO.output(led_left, 1)
    GPIO.output(led_right, 1)
    while pygame.mixer.music.get_busy() == True:
        GPIO.output(led_left, 1)
        GPIO.output(led_right, 1)
        continue

    GPIO.output(led_left, 0)
    GPIO.output(led_right, 0)

def start_alarm():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(led_left, GPIO.OUT)
    GPIO.setup(led_right, GPIO.OUT)

    while pygame.mixer.music.get_busy() == True:
        GPIO.output(led_left, 1)
        GPIO.output(led_right, 0)
        time.sleep(0.5)
        GPIO.output(led_left, 0)
        GPIO.output(led_right, 1)
        time.sleep(0.5)
        continue

    GPIO.output(led_left, 0)
    GPIO.output(led_right, 0)

if __name__ == '__main__':
    # test1.py executed as script
    # do something
    start_speak()