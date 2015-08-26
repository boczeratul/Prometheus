import RPi.GPIO as GPIO
import time
# import random
import common
import light
import pygame

rest_time = 30

def danboard():
    index = 1

    pygame.mixer.init()

    while True:
        if pygame.mixer.music.get_busy() == True:
            time.sleep(rest_time)
            continue
        common.play_mp3('./assets/r2d2_' + str(index) + '.mp3')
        light.start_speak()
        index += 1
        if index == 11:
            index = 1
        time.sleep(rest_time)

if __name__ == '__main__':
    # test1.py executed as script
    # do something
    danboard()