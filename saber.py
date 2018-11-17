import config
import neopixel as neo
import time

class Saber(object):
    def __init__(self):
        self.strand_lights = config.SIDE_1_LEDS + config.SIDE_2_LEDS + config.SIDE_3_LEDS + config.SIDE_4_LEDS
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
        print('setting led {0}'.format(line * number))
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


    def run(self):
        print('running')
        while True:

            for n in range(50):
                self.set_led(1, n, neo.Color(200, 0, 0), False)
                self.set_led(2, n, neo.Color(200, 0, 0), False)
                self.set_led(3, n, neo.Color(200, 0, 0), False)
                self.set_led(4, n, neo.Color(200, 0, 0), True)
                time.sleep(100 / 1000.0)

            for n in range(50):
                self.set_led(1, n, neo.Color(0, 0, 0), False)
                self.set_led(2, n, neo.Color(0, 0, 0), False)
                self.set_led(3, n, neo.Color(0, 0, 0), False)
                self.set_led(4, n, neo.Color(0, 0, 0), True)
                time.sleep(200 / 1000.0)

