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
        print('setting')
        if line == 2 and number == 50:
            print('Broken light')
            return None

        if line > 2:
            print('Setting pixel {0} >> line {1} number {2}'.format(
                line * number - 1,
                line,
                number
            ))
            self.strand.setPixelColor(line * number - 1, color)
        else:
            print('Setting pixel {0} >> line {1} number {2}'.format(
                line * number,
                line,
                number
            ))
            self.strand.setPixelColor(line * number, color)

        if show:
            self.strand.show()


    def run(self):
        print('running')
        while True:

            for n in range(50):
                self.set_led(0, n, neo.Color(200, 0, 0), False)
                self.set_led(1, n, neo.Color(200, 0, 0), False)
                self.set_led(2, n, neo.Color(200, 0, 0), False)
                self.set_led(3, n, neo.Color(200, 0, 0), True)
                time.sleep(50 / 1000.0)

            for n in range(50):
                self.set_led(0, n, neo.Color(0, 0, 0), False)
                self.set_led(1, n, neo.Color(0, 0, 0), False)
                self.set_led(2, n, neo.Color(0, 0, 0), False)
                self.set_led(3, n, neo.Color(0, 0, 0), True)
                time.sleep(50 / 1000.0)

