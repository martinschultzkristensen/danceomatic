#!/usr/bin/env python3

#!/usr/bin/env python3

import omxplayer
from pathlib import Path
from time import sleep

#THE LIST SPECIFICES THE AUDIO OUTPUT TO JACK!!!
player = omxplayer.player.OMXPlayer("/home/pi/Desktop/elephant.mp4", ['-o','local', '--loop'])

sleep(10) #How long time it should play before quit.


player.quit()