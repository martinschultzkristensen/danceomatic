from omxplayer import OMXPlayer
from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode (GPIO.BOARD)
GPIO.setwarnings (False)
up = 12
down = 11
enter = 7

#All Gpio's as input and pull up
GPIO.setup(up,GPIO.IN,pull_up_down=GPIO.PUD_UP) # Set button "up" as input and Activate pull up resistor
GPIO.setup(down, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(enter, GPIO.IN, pull_up_down = GPIO.PUD_UP)

#make a list

playerA = OMXPlayer('/home/pi/Desktop/video/ai.mp4', args=['-o', 'local', '--loop'])
playerB = OMXPlayer('/home/pi/Desktop/video/Culture4Fun.mp4', args=['-o', 'local', '--loop'])
playerC = OMXPlayer('/home/pi/Desktop/video/MT.mp4', args=['-o', 'local', '--loop'])

playerA.play()
playerA.set_video_pos(200, 200, 627, 440)

while True:
    if GPIO.input(up) == 0: #set in interrupt
        if playerA.is_playing() == True:
            playerB.set_video_pos(200, 200, 627, 440)
            playerB.play()
        elif playerB.is_playing == True:
            playerC.set_video_pos(200, 200, 627, 440)
            playerC.play()
        else:
            playerA.set_video_pos(200, 200, 627, 440)
            playerA.play()

    if GPIO.input(down) == 0:  # set in interrupt
        if playerC.is_playing() == True:
            playerB.play()
            playerB.set_video_pos(200, 200, 627, 440)
        elif playerB.is_playing == True:
            playerA.play()
            playerA.set_video_pos(200, 200, 627, 440)
        else:
            playerC.play()
            playerC.set_video_pos(200, 200, 627, 440)

    if GPIO.input(enter) == 0:
        if playerA.is_playing() == True:
            playerA.quit()
        elif playerB.is_playing() == True:
            playerB.quit()
        elif playerC.is_playing() == True:
            playerC.quit()


GPIO.cleanup()