#!/usr/bin/env python3

import omxplayer
from pathlib import Path
from time import sleep


#THE LIST SPECIFIES THE AUDIO OUTPUT TO JACK!!!


VIDEO_PATH = Path("/home/pi/Desktop/elephant.mp4")




player = omxplayer.player.OMXPlayer(VIDEO_PATH, ['-o', 'local'])

#set_video_pos(x1, y1, x2, y2)
player.set_video_pos(100,100,200,200)
print("hey")
sleep(2)
player.play(VIDEO_PATH)
sleep(5)
player.pause()
sleep(2)
player.play()
sleep(2)
player.quit()
