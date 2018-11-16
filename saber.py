import sys

sys.path.append('~/git_clones/rpi_ws281x/python')

import config
import neopixel as neo
import time

class Saber(object):
    def __init__(self):
        self.strand_lights = config.SIDE_1_LEDS + config.SIDE_2_LEDS + config.SIDE_3_LEDS + config.SIDE_4_LEDS
        self.strand = neo.Adafruit.NeoPixel(self.strand_lights,
                                            config.LED_PIN,
                                            config.LED_FREQ,
                                            config.LED_DMA,
                                            config.LED_INVERT,
                                            config.LED_BRIGHTNESS,
                                            config.LED_CHANNEL
                                            )

    def run(self):
        while True:
            for i in range(self.strand_lights):
                self.strand.setPixelColor(i, neo.Color(255, 0, 0))
                self.strip.show()
                time.sleep(50/1000.0)
