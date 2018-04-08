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
#vidc = '/home/pi/Desktop/video/MT.mp4'
default = '/home/pi/Desktop/video/Hej-Nihao.mp4'

import RPi.GPIO as GPIO


#set up GPIO using BCM numbering

GPIO.setmode(GPIO.BCM)
#All Gpio's as input and pull up


GPIO.setup(2, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(3, GPIO.IN, pull_up_down = GPIO.PUD_UP)
#GPIO.setup(4, GPIO.IN, pull_up_down = GPIO.PUD_UP)


player = OMXPlayer(default,args=['--no-osd','--blank'],)

while True:

      if GPIO.input(2) ==0:

           player.load(vida)
           print("gpio 2")
           player.play()
           #sleep(5)

      if (GPIO.input(3) == 0):

            player.load(vidb)
            print("gpio 3")
            player.play()
           # sleep(5)



#      if (GPIO.input(4) == 0):
 #           player.load(vidc)
  #          print("gpio 4")
   #         player.play()
            #sleep(5)



GPIO.cleanup()
