from microbit import *
import neopixel
 
#Neopixel with 8 LEDs
neo = neopixel.NeoPixel(pin0, 8)
 
while True:
  neo[0] = (255, 0, 0)
  neo[1] = (0, 255, 0)
  neo[2] = (0, 0, 255)
  neo[3] = (128, 0, 0)
  neo[4] = (0, 128, 0)
  neo[5] = (0, 0, 128)
  neo[6] = (128, 128, 0)
  neo[7] = (0,0,0)
  neo.show()
  sleep(250)
