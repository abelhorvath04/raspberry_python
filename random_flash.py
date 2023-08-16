from sense_hat import SenseHat
import time
from time import sleep
from random import randint

sense = SenseHat()


text_color = (255, 255, 255)
bg_color = (0, 0, 0)
white = (255,255,255)
red = (255,0,0)

try:
    while True:
                
        num1 = randint(0,255)
        num2 = randint(0,255)
        num3 = randint(0,255)
        color = (num1,num2,num3)
        space1 = randint(0,7)
        space2 = randint(0,7) 
        
        sense.set_pixel(space1,space2,color)
        
except KeyboardInterrupt:
    sense.clear()
    
print("Script Terminated")


