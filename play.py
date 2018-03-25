#!/usr/bin/env python3

import omxplayer
from pathlib import Path
from time import sleep

VIDEO_PATH = Path("/home/pi/Desktop/elephant.mp4", args['-o', 'local'])

player = omxplayer.player.OMXPlayer(VIDEO_PATH)

sleep(5)

player.quit()