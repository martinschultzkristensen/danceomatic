import RPi.GPIO as GPIO
import time 

import omxplayer
from pathlib import Path

GPIO.setmode (GPIO.BOARD)
GPIO.setwarnings (False)


button1=12  # Descriptive Variable for pin 12
GPIO.setup(button1,GPIO.IN,pull_up_down=GPIO.PUD_UP) # Set button1 as input and Activate pull up resisor


while(1): # Create an infinite loop
    player = omxplayer.player.OMXPlayer("/home/pi/Desktop/elephant.mp4", ['-o', 'local'])
    if GPIO.input(button1)==0: # button 1 will report 0 if it is presses
            time.sleep(.1)
            print ("Button Pressed")
    player.quit()
 
    

player.quit()
GPIO.cleanup
                
                
