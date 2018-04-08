#!/usr/bin/env python3

import omxplayer
from pathlib import Path
from time import sleep


#THE LIST SPECIFIES THE AUDIO OUTPUT TO JACK!!!



player.quit()

VIDEO_PATH = Path("/home/pi/Desktop/elephant.mp4")

#set_video_crop(x1, y1, x2, y2)
#cropVideo = (100,100,200,200)

player = omxplayer.player.OMXPlayer(VIDEO_PATH, ['-o', 'local', '--win 100 100 200 200'])


sleep(5)
player.pause()
sleep(2)
player.play()
sleep(2)
player.quit()
