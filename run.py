import argparse
import time
from saber import Saber, rgb

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
    parser.add_argument('-b', '--brightness', default=255, help='the max brightness of the strip')
    args = parser.parse_args()

    print('Press Ctrl-C to quit.')
    if not args.clear:
        print('Use "-c" argument to clear LEDs on exit')

    saber = Saber(args.brightness)

    try:
        while True:
            saber.swipe(rgb(255, 0, 0), 5 / 10000.0)
            saber.reverse_swipe(rgb(0, 0, 0), 5 / 10000.0)

            saber.swipe(rgb(0, 0, 255), 5 / 10000.0)
            saber.reverse_swipe(rgb(0, 0, 0), 5 / 10000.0)

            saber.swipe(rgb(0, 255, 0), 5 / 10000.0)
            saber.reverse_swipe(rgb(0, 0, 0), 5 / 10000.0)
    except KeyboardInterrupt:
        if args.clear:
            for j in range(255):
                for i in range(saber.strand_lights):
                    saber.reduce_led(i, 1)
                saber.strand.show()
                time.sleep(1 / 1000.0)

