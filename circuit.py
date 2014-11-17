#!/usr/bin/env python
import sys
from components.led import LED, FlashingLED
from RPi import GPIO

def setup_board():
    print "setting up board"
    GPIO.setmode(GPIO.BOARD)

def main(args):
    print "start"
    setup_board()
    red = LED(pin=12)
    flashing = FlashingLED(pin=12, interval=0.1)
    import IPython; IPython.embed()
    print "done"

if __name__ == "__main__":
    args = {}
    main(args)
