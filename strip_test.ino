#include <Adafruit_NeoPixel.h>

#define PIN 4	 // input pin Neopixel is attached to

#define NUMPIXELS 6 // number of neopixels in Ring

Adafruit_NeoPixel pixels = Adafruit_NeoPixel(NUMPIXELS, PIN, NEO_GRB + NEO_KHZ800);

int redColor = 0;
int greenColor = 0;
int blueColor = 0;
int delayval = 100;

void setup() {
  pixels.begin(); // Initializes the NeoPixel library.
  pixels.show();
}

void loop() {
  for(int i=0;i<NUMPIXELS;i++){

    // pixels.Color takes RGB values, from 0,0,0 up to 255,255,255
    pixels.setPixelColor(i, pixels.Color(redColor, greenColor, blueColor)); // Moderately bright green color.

    pixels.show(); // This sends the updated pixel color to the hardware.

    delay(delayval); // Delay for a period of time (in milliseconds).

  }
  pixels.clear();
  delay(delayval);
}
