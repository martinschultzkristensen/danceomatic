#!/usr/bin/env python3

import omxplayer
from pathlib import Path
from time import sleep


#THE LIST SPECIFIES THE AUDIO OUTPUT TO JACK!!!
player = omxplayer.player.OMXPlayer("/home/pi/Desktop/elephant.mp4", ['-o','local', '--loop'])

sleep(10) #How long time it should play before quit.


player.quit()

VIDEO_PATH = Path("/home/pi/Desktop/elephant.mp4")

player = omxplayer.player.OMXPlayer(VIDEO_PATH, ['-o', 'local'])

sleep(5)
player.pause()
sleep(2)
player.play()
sleep(2)
player.quit()
