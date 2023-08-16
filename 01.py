from sense_hat import SenseHat

sense = SenseHat()

text_color = (255, 255, 255)
bg_color = (0, 0, 0)
scroll_speed = 0.05

message = "Kedves Vendegek, taka!"
sense.show_message(message, text_colour=text_color, back_colour=bg_color, scroll_speed=scroll_speed)