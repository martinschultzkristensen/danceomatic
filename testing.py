from omxplayer.player import OMXPlayer
from pathlib import Path
from time import sleep
import logging
#import RPi.GPIO as GPIO

#GPIO.setmode (GPIO.BOARD)
#GPIO.setwarnings (False)

VIDEO_PATH = "/home/pi/Desktop/elephant.mp4"
player_log = logging.getLogger("Player1")


intro = OMXPlayer(VIDEO_PATH, ['-o', 'local'], dbus_name='org.mpris.MediaPlayer2.omxplayer1')

intro.playEvent += lambda _: player_log.info("Play")
intro.pauseEvent += lambda _: player_log.info("Pause")
intro.stopEvent += lambda _: player_log.info("Stop")

sleep(2.5)

intro.set_position(5)
intro.pause()

sleep(1)
intro.set_aspect_mode("letterbox")
intro.set_video_pos(50,100,1000,1000)

intro.play()

sleep(5)
intro.quit()