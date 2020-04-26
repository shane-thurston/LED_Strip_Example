from microbit import *
import neopixel
 
#Neopixel with 8 LEDs
neo = neopixel.NeoPixel(pin0, 8)
 
while True:
  #Iterate over each LED in the strip
  for pixel_id in range(0, len(neo)):
    neo[pixel_id] = (255, 0, 0)
    neo.show()
    sleep(250)
    neo[pixel_id] = (0, 255, 0)
    neo.show()
    sleep(250)
    neo[pixel_id] = (0, 0, 255)
    neo.show()
    sleep(250)
