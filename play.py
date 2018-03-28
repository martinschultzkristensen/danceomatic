#!/usr/bin/env python3

import omxplayer
from pathlib import Path
from time import sleep

VIDEO_PATH = Path("/home/pi/Desktop/elephant.mp4")

player = omxplayer.player.OMXPlayer(VIDEO_PATH, ['-o', 'local'])

sleep(5)
player.pause()
sleep(2)
player.play()
sleep(2)
player.quit()
