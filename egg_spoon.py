from microbit import *

egg_x = 2
egg_y = 2

while True:
  if egg_y > 4 or egg_x > 4 or egg_x < 0 or egg_y < 0:
    display.show(Image.SKULL)
    sleep(2000)
    egg_x = 2
    egg_y = 2
  else:
    display.clear()
    display.set_pixel(egg_x, egg_y, 9)
    sleep(300)
  if accelerometer.get_x() > 200:
    egg_x = egg_x + 1
  elif accelerometer.get_x() < -200:
    egg_x = egg_x - 1
  if accelerometer.get_y() > 200:
    egg_y = egg_y + 1
  elif accelerometer.get_y() < -200:
    egg_y = egg_y - 1
