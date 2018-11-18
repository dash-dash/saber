import argparse
import time
from saber import Saber, rgb

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
    args = parser.parse_args()

    print('Press Ctrl-C to quit.')
    if not args.clear:
        print('Use "-c" argument to clear LEDs on exit')

    saber = Saber()

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
            saber.swipe(rgb(0, 0, 0), 200 / 1000.0)
            for j in range(255):
                for i in range(saber.strand_lights):
                    saber.reduce_led(i, 1)
                saber.strand.show()
                time.sleep(1 / 1000.0)