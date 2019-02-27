import argparse
from threading import Thread
from queue import Queue, Empty
import time

from saber import Saber, rgb

PATTERNS = ['r', 'g', 'b', 'rand', 's']


def run(thread_name, queue, brightness, freq):
    saber = Saber(brightness)
    print('Running')
    current_pattern = 'g'
    while True:
        try:
            item = queue.get(False)
            # if item in PATTERNS:
            #     current_pattern = item
            if item is None:
                break
        except Empty:
            pass

        print(current_pattern)

        if current_pattern == 'r':
            saber.swipe(rgb(255, 0, 0), freq / 1000.0)
            saber.reverse_swipe(rgb(0, 0, 0), freq / 1000.0)

        elif current_pattern == 'g':
            saber.swipe(rgb(0, 255, 0), freq / 1000.0)
            saber.reverse_swipe(rgb(0, 0, 0), freq / 1000.0)

        elif current_pattern == 'b':
            saber.swipe(rgb(0, 0, 255), freq / 1000.0)
            saber.reverse_swipe(rgb(0, 0, 0), freq / 1000.0)

        elif current_pattern == 'rand':
            saber.random(freq / 1000.0)

        elif current_pattern.startswith('s'):
            print('up_down')
            vals = current_pattern.slit(',')
            r, g, b, s, size = vals[1], vals[2], vals[3], vals[4], vals[5]
            saber.up_down(rgb(r, g, b), s / 1000.0, size)

    saber.swipe(rgb(0, 0, 0), freq / 1000.0)


def key_input(queue):
    choice = input("")
    if choice == 'q':
        queue.put(None)
        return 0
    queue.put(choice)
    return 1


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
    parser.add_argument('-b', '--brightness', default=255, help='the max brightness of the strip', type=int)
    parser.add_argument('-f', '--frequency', default=50, help='frequency at witch it runs', type=float)
    args = parser.parse_args()

    print('Press Ctrl-C to quit.')
    if not args.clear:
        print('Use "-c" argument to clear LEDs on exit')
    print('brightness: {}, frequency: {}'.format(args.brightness, args.frequency))
    q = Queue()
    thread = Thread(target=run, args=('run', q, args.brightness, args.frequency))
    thread.start()

    while key_input(queue=q):
        pass
