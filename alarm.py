import RPi.GPIO as GPIO
import time
import common

repeat = 3
speaker = 4
led = 17
default_alarm = './assets/warning_1.mp3'

def alarm_mp3_with_light(mp3):
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(led, GPIO.OUT)
    GPIO.output(led, 1)

    common.play_mp3(mp3)

    GPIO.output(led, 0)
    GPIO.cleanup()

def alarm_mp3(mp3):
    pygame.mixer.init()
    pygame.mixer.music.load(mp3)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue
    pygame.mixer.quit()

# def alarm():
#     GPIO.setwarnings(False)
#     GPIO.setmode(GPIO.BCM)
#     GPIO.setup(speaker, GPIO.OUT)

#     # Warm up alarm
#     GPIO.output(speaker, 1)
#     time.sleep(2)

#     for x in range(0, repeat):
#         GPIO.output(speaker, 0)
#         time.sleep(0.5)
#         GPIO.output(speaker, 1)
#         time.sleep(2)

#     GPIO.output(speaker, 0)

#     GPIO.cleanup()

if __name__ == '__main__':
    # test1.py executed as script
    # do something
    alarm_mp3_with_light(default_alarm)
