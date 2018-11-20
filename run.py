import argparse
from threading import Thread
from queue import Queue, Empty
import time

from saber import Saber, rgb

patterns = ['r', 'g', 'b']


def run(thread_name, queue, brightness):
    saber = Saber(brightness)
    print('Running')
    current_pattern = 'g'
    while True:
        try:
            item = queue.get()
            if item in patterns:
                current_pattern = item
            elif item is None:
                break
        except Empty:
            pass

        if current_pattern == 'r':
            print('Pattern R')
            saber.swipe(rgb(255, 0, 0), 5 / 1000.0)
            saber.reverse_swipe(rgb(0, 0, 0), 5 / 1000.0)

        elif current_pattern == 'g':
            print('Pattern G')
            saber.swipe(rgb(0, 255, 0), 5 / 1000.0)
            saber.reverse_swipe(rgb(0, 0, 0), 5 / 1000.0)

        elif current_pattern == 'b':
            print('Pattern B')
            saber.swipe(rgb(0, 0, 255), 5 / 1000.0)
            saber.reverse_swipe(rgb(0, 0, 0), 5 / 1000.0)

    saber.swipe(rgb(0, 0, 0), 5 / 1000.0)


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
    args = parser.parse_args()

    print('Press Ctrl-C to quit.')
    if not args.clear:
        print('Use "-c" argument to clear LEDs on exit')

    q = Queue()
    thread = Thread(target=run, args=('run', q, args.brightness))
    thread.start()

    while key_input(queue=q):
        pass
