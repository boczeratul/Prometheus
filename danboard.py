import RPi.GPIO as GPIO
import time
import random
import common

led = 17

def danboard():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(led, GPIO.OUT)

    index = 1

    while True:
        GPIO.output(led, 1)
        common.play_mp3('./assets/r2d2_' + str(index) + '.mp3')
        GPIO.output(led, 0)
        index += 1
        if index == 11:
            index = 1
        time.sleep(20)
    
    GPIO.cleanup()

if __name__ == '__main__':
    # test1.py executed as script
    # do something
    danboard()