from sense_hat import SenseHat
import time
from random import randint

sense = SenseHat()

text_color = (255,255,255)
bg_color = (0,0,0)
white = text_color
red = (255,0,0)
scroll_speed = 0.07
repetitions = 0

message = "Szia Cico!"

def my_message():
    sense.show_message(message, text_colour=text_color, back_colour=bg_color, scroll_speed=scroll_speed)

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


heart2 = [
    0,0,0,0,0,0,0,0,
    0,1,0,0,0,0,1,0,
    1,1,1,0,0,1,1,1,
    1,1,1,1,1,1,1,1,
    0,1,1,1,1,1,1,0,
    0,0,1,1,1,1,0,0,
    0,0,0,1,1,0,0,0,
    0,0,0,0,0,0,0,0
]


heart3 = [
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,1,0,0,0,0,1,0,
    1,1,1,0,0,1,1,1,
    1,1,1,1,1,1,1,1,
    0,1,1,1,1,1,1,0,
    0,0,1,1,1,1,0,0,
    0,0,0,1,1,0,0,0,
]

def hearts():
    while True:
        for y in range(8):
            for x in range(8):
                pixel_index = y * 8 + x
                if heart[pixel_index] == 1:
                    sense.set_pixel(x,y,white)
                else:
                    sense.set_pixel(x,y,red)
                    
        time.sleep(1.1)
        sense.clear()
        
        for y in range(8):
            for x in range(8):
                pixel_index = y * 8 + x
                if heart2[pixel_index] == 1:
                    sense.set_pixel(x,y,red)
                else:
                    sense.set_pixel(x,y,white)
                    
        time.sleep(1.1)
        sense.clear()
                    
                    
        for y in range(8):
            for x in range(8):
                pixel_index = y * 8 + x
                if heart3[pixel_index] == 1:
                    sense.set_pixel(x,y,white)
                else:
                    sense.set_pixel(x,y,red)
                    
        time.sleep(1.1)
        sense.clear()
        
        for y in range(8):
            for x in range(8):
                pixel_index = y * 8 + x
                if heart2[pixel_index] == 1:
                    sense.set_pixel(x,y,red)
                else:
                    sense.set_pixel(x,y,white)
                    
        time.sleep(1.1)
        sense.clear()
        
def color_flash():
    
        num1 = randint(0,255)
        num2 = randint(0,255)
        num3 = randint(0,255)
        color = (num1,num2,num3)
        space1 = randint(0,7)
        space2 = randint(0,7) 
        
        sense.set_pixel(space1,space2,color)
        time.sleep(0.005)
        sense.clear()
        
for _ in range(2):
    while repetitions < 200:
        color_flash()
        repetitions += 1
    my_message()
    while repetitions < 200:
        color_flash()
        repetitions += 1
    hearts()
    while repetitions < 200:
        color_flash()
        repetitions += 1
