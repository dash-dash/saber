import argparse
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
        saber.run()
    except KeyboardInterrupt:
        if args.clear:
            saber.swipe(rgb(0, 0, 0), 200 / 1000.0)