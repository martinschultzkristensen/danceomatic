import RPi.GPIO as GPIO
import time 

import omxplayer
from pathlib import Path

GPIO.setmode (GPIO.BOARD)
GPIO.setwarnings (False)
button1=12  # Descriptive Variable for pin 12
GPIO.setup(button1,GPIO.IN,pull_up_down=GPIO.PUD_UP) # Set button1 as input and Activate pull up resistor

vida = "/home/pi/Desktop/elephant.mp4"

player = omxplayer.player.OMXPlayer(default, ['-o', 'local']) #arg local push sound to jack
#set_video_pos(x1, y1, x2, y2)
player.set_video_pos(200,200,627,440) #vida er 854 × 480px. Divide with two + x1 and y1
while True:
    if GPIO.input(button1)==0: # button 1 will report 0 if it is presses
        time.sleep(.1)
        print("Button Pressed")
        player.quit()
 
    

player.quit()
GPIO.cleanup