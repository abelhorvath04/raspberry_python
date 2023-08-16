from sense_hat import SenseHat
import time
from time import sleep
from random import randint

sense = SenseHat()


text_color = (255, 255, 255)
bg_color = (0, 0, 0)
white = (255,255,255)
red = (255,0,0)

heart = [
    0,1,0,0,0,0,1,0,
    1,1,1,0,0,1,1,1,
    1,1,1,1,1,1,1,1,
    0,1,1,1,1,1,1,0,
    0,0,1,1,1,1,0,0,
    0,0,0,1,1,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
]

try:
    
    while True:
        
        for y in range(8):
            for x in range (8):
                pixel_index = y * 8 + x
                if heart[pixel_index] == 1:
                    sense.set_pixel(x,y,red)
                else:
                    sense.set_pixel(x,y,white)
        time.sleep(2)
    
        for y in range(8):
            for x in range (8):
                pixel_index = y * 8 + x
                if heart[pixel_index] == 1:
                    sense.set_pixel(x,y,white)
                else:
                    sense.set_pixel(x,y,red)
        time.sleep(2)
        
        num1 = randint(0,255)
        num2 = randint(0,255)
        num3 = randint(0,255)
        color = (num1,num2,num3)
        space1 = randint(0,7)
        space2 = randint(0,7) 
        
        sense.set_pixel(space1,space2,color)
        sleep(1)
        
except KeyboardInterrupt:
    sense.clear()
    
print("Script Terminated")

