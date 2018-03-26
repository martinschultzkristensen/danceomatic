import RPi.GPIO as GPIO
import time 



GPIO.setmode (GPIO.BOARD)
GPIO.setwarnings (False)
import omxplayer
from pathlib import Path

button1=16  # Descriptive Variable for pin 16
button2=12  # Descriptive Variable for pin 12
GPIO.setup(button1,GPIO.IN,pull_up_down=GPIO.PUD_UP) # Set button1 as input and Activate pull up resistor
GPIO.setup(button2,GPIO.IN,pull_up_down=GPIO.PUD_UP) # Set button2 as input and Activate pull up resisor


while(1): # Create an infinite loop
    player = omxplayer.player.OMXPlayer("/home/pi/Desktop/elephant.mp4", ['-o', 'local'])
    if GPIO.input(button2)==0: # button 2 will report 0 if it is presses
            time.sleep(.1)
            print ("Button 2 Pressed")
    player.quit()

player.quit()
GPIO.cleanup
                
                
