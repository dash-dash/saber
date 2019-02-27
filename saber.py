import config
import neopixel as neo
import time
import random


def rgb(r, g, b):
    return neo.Color(g, r, b)


def intensity_change(original, value, direction):
    new = original
    if direction == 0:  # down
        if original >= value:
            new = original - value
    else:  # up
        if original <= 255 + value:
            new = original + value
    return new


class Saber(object):
    def __init__(self, max_brightness=255):
        self.strand_lights = sum(n['length'] for n in config.LINES)
        self.strand = neo.Adafruit_NeoPixel(self.strand_lights,
                                            config.LED_PIN,
                                            config.LED_FREQ,
                                            config.LED_DMA,
                                            config.LED_INVERT,
                                            max_brightness,
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

    def increase_led(self, number, value, color='ALL'):
        r, g, b = self.get_rgb(number)

        if color == config.COLORS[0]:
            r = intensity_change(r, value, 1)
        elif color == config.COLORS[1]:
            g = intensity_change(g, value, 1)
        elif color == config.COLORS[2]:
            b = intensity_change(b, value, 1)
        else:
            r = intensity_change(r, value, 1)
            g = intensity_change(g, value, 1)
            b = intensity_change(b, value, 1)

        self.strand.setPixelColor(number, rgb(r, g, b))

    def reduce_led(self, number, value, color='ALL'):
        r, g, b = self.get_rgb(number)

        if color == config.COLORS[0]:
            r = intensity_change(r, value, 0)
        elif color == config.COLORS[1]:
            g = intensity_change(g, value, 0)
        elif color == config.COLORS[2]:
            b = intensity_change(b, value, 0)
        else:
            r = intensity_change(r, value, 0)
            g = intensity_change(g, value, 0)
            b = intensity_change(b, value, 0)

        self.strand.setPixelColor(number, rgb(r, g, b))

    def get_rgb(self, led):
        int_val = self.strand.getPixelColor(led)
        hex_val = hex(int_val)[2::]
        hex_string = '0' * (6 - len(hex_val)) + hex_val
        g = hex_string[:2]
        r = hex_string[2:4]
        b = hex_string[4:6]

        return int(r, 16), int(g, 16), int(b, 16)

    def set_section(self, color, line, start, end):
        end = min(end, line['length'])
        for i in range(start):
            self.set_led(line['number'], i, rgb(0, 0, 0), False)
        for i in range(start, end):
            self.set_led(line['number'], i, color, False)
        for i in range(end, line['length']):
            self.set_led(line['number'], i, rgb(0, 0, 0), False)

    def up_down(self, color, speed, size):
        for i in range(50):
            self.set_section(color, config.LINE_1, i, i + size)
            self.set_section(color, config.LINE_2, i, i + size)
            self.set_section(color, config.LINE_3, i, i + size)
            self.set_section(color, config.LINE_4, i, i + size)
            self.strand.show()
            time.sleep(speed)
        for i in range(50):
            c = 49 - i
            self.set_section(color, config.LINE_1, c, c + size)
            self.set_section(color, config.LINE_2, c, c + size)
            self.set_section(color, config.LINE_3, c, c + size)
            self.set_section(color, config.LINE_4, c, c + size)
            self.strand.show()
            time.sleep(speed)


    def swipe(self, color, speed):
        for n in range(50):
            self.set_led(1, n, color, False)
            self.set_led(2, n, color, False)
            self.set_led(3, n, color, False)
            self.set_led(4, n, color, True)
            time.sleep(speed)

    def reverse_swipe(self, color, speed):
        for n in range(50):
            self.set_led(1, 49 - n, color, False)
            self.set_led(2, 49 - n, color, False)
            self.set_led(3, 49 - n, color, False)
            self.set_led(4, 49 - n, color, True)
            time.sleep(speed)

    def random(self, speed, perc_off=0.7, leds=5):
        on_off = random.random()
        color = rgb(0, 0, 0)
        if on_off > perc_off:
            i = random.randint(0, 16777214)
            h = hex(i)[2::]
            h = '0' * (6 - len(h)) + h
            color = rgb(int(h[:2], 16), int(h[2:4], 16), int(h[4:6], 16))

        line = random.randint(1, 4)
        start_led = random.randint(0, 49)
        end_led = min(start_led + leds, 50)

        for i in range(start_led, end_led):
            self.set_led(line, i, color, True)

        time.sleep(speed)

    def kit(self, side, length, color, background=rgb(0,0,0), speed=50/1000.0):
        for i in range(50):
            self.set_led(side, i, color, False)

    def test_run(self):
        print('running')
        while True:

            self.swipe(rgb(255, 0, 0), 5 / 10000.0)
            self.reverse_swipe(rgb(0, 0, 0), 5 / 10000.0)

            self.swipe(rgb(0, 0, 255), 5 / 10000.0)
            self.reverse_swipe(rgb(0, 0, 0), 5 / 10000.0)

            self.swipe(rgb(0, 255, 0), 5 / 10000.0)
            self.reverse_swipe(rgb(0, 0, 0), 5 / 10000.0)

