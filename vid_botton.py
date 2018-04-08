#From https://github.com/willprice/python-omxplayer-wrapper/issues/85
#Change videopath & GPIO pin test.

#!/usr/bin/env python2
import os.path
from time import sleep
import subprocess
import os
from omxplayer import OMXPlayer
vida = '/home/pi/Desktop/video/ai.mp4'
vidb = '/home/pi/Desktop/video/Culture4Fun.mp4'
vidc = '/home/pi/Desktop/video/MT.mp4'
default = '/home/pi/Desktop/video/Hej-Nihao.mp4'

import RPi.GPIO as GPIO


#set up GPIO using BCM numbering

GPIO.setmode (GPIO.BOARD)
GPIO.setwarnings (False)


#All Gpio's as input and pull up
GPIO.setup(12,GPIO.IN,pull_up_down=GPIO.PUD_UP) # Set button1 as input and Activate pull up resistor
GPIO.setup(11, GPIO.IN, pull_up_down = GPIO.PUD_UP)



player = OMXPlayer(default,args=['-o', 'local', '--loop'],)
player.set_video_pos(200,200,627,440) #video files are ?854 × 480px.? Divide with two + x1 and y1
while True:
    #player = OMXPlayer(default, args=['-o', 'local'], )
    #player.set_video_pos(200, 200, 627, 440)

    if GPIO.input(12) ==0:
        player.load(vida)
        player.set_video_pos(200,200,627,440)
        print("button1 pushed")
        player.play()
        #sleep(5)

    elif GPIO.input(11) ==0:
        player.load(vidb)
        player.set_video_pos(200,200,627,440)
        print("button2 pushed")
        player.play()
        #sleep(5)


#      if (GPIO.input(4) == 0):
 #           player.load(vidc)
  #          print("gpio 4")
   #         player.play()
            #sleep(5)


# Kill the `omxplayer` process gracefully.
player.quit()
GPIO.cleanup()
