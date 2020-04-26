from microbit import *
import neopixel
from random import randint

# Setup the Neopixel strip on pin0 with a length of 8 pixels
neo = neopixel.NeoPixel(pin0, 8)

while True:
  #Iterate over each LED in the strip
  for pixel_id in range(0, len(neo)):
    red = randint(0, 60)
    green = randint(0, 60)
    blue = randint(0, 60)
    
    # Assign the current LED a random red, green and blue value between 0 and 60
    neo[pixel_id] = (red, green, blue)

    # Display the current pixel data on the Neopixel strip
    neo.show()
    sleep(100)
