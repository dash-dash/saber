import config
import neopixel as neo
import time

def rgb(r, g, b):
    return neo.Color(g, r, b)

class Saber(object):
    def __init__(self):
        self.strand_lights = sum(config.SIDES)
        self.strand = neo.Adafruit_NeoPixel(self.strand_lights,
                                            config.LED_PIN,
                                            config.LED_FREQ,
                                            config.LED_DMA,
                                            config.LED_INVERT,
                                            config.LED_BRIGHTNESS,
                                            config.LED_CHANNEL
                                            )
        self.strand.begin()

    def set_led(self, line, number, color, show):

        if line == 1:
            self.strand.setPixelColor(number, color)
        elif line == 2:
            self.strand.setPixelColor(99 - number, color)
        elif line == 3:
            if number != 49:
                self.strand.setPixelColor(100 + number, color)
        elif line == 4:
            self.strand.setPixelColor(198 - number, color)

        if show:
            self.strand.show()

    def swipe(self, color, speed):
        for n in range(50):
            self.set_led(1, n, color, False)
            self.set_led(2, n, color, False)
            self.set_led(3, n, color, False)
            self.set_led(4, n, color, True)
            time.sleep(speed)

    def reverse_swipe(self, color, speed):
        for n in range(50):
            self.set_led(4, n, color, False)
            self.set_led(3, n, color, False)
            self.set_led(2, n, color, False)
            self.set_led(1, n, color, True)
            time.sleep(speed)

    def kit(self, side, length, color, background=rgb(0,0,0), speed=50/1000.0):
        for i in range(50):
            self.set_led(side, i, color, False)

    def run(self):
        print('running')
        while True:

            self.swipe(rgb(255, 0, 0), 5 / 10000.0)
            self.reverse_swipe(rgb(0, 0, 0), 5 / 10000.0)

            self.swipe(rgb(0, 0, 255), 5 / 10000.0)
            self.reverse_swipe(rgb(0, 0, 0), 5 / 10000.0)

            self.swipe(rgb(0, 255, 0), 5 / 10000.0)
            self.reverse_swipe(rgb(0, 0, 0), 5 / 10000.0)

