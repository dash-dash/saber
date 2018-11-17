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


    def set_led(self, line, number, color):
        if not line == 2 and number == 50:
            if line > 2:
                print('Setting pixel {0} >> line {1} number {2}'.format(
                    line * number - 1,
                    line,
                    number
                ))
                self.strand.setPixelColor(line * number - 1, color)
                self.strand.show()
            else:
                print('Setting pixel {0} >> line {1} number {2}'.format(
                    line * number - 1,
                    line,
                    number
                ))
                self.strand.setPixelColor(line * number, color)
                self.strand.show()


    def run(self):
        print('running')
        while True:
            for l in range(4):
                for n in range(50):
                    self.set_led(l, n, neo.Color(200, 0, 0))
                    time.sleep(50 / 1000.0)
            for l in range(4):
                for n in range(50):
                    self.set_led(l, n, neo.Color(0, 0, 0))
                    time.sleep(50 / 1000.0)

