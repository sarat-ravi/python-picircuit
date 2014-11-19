#!/usr/bin/env python
import sys
from RPi import GPIO
from picircuit.components.led import LED, FlashingLED
from picircuit.components.button import Button

def setup_board():
    print "setting up board"
    GPIO.setmode(GPIO.BCM)

def main(args):
    print "start"
    setup_board()
    red = LED(pin=18)
    flashing = FlashingLED(pin=18, interval=0.1)
    button = Button(pin=23)
    button.link_component(flashing, mode="sticky", trigger="rising")
    import IPython; IPython.embed()
    GPIO.cleanup()
    print "done"

if __name__ == "__main__":
    args = {}
    main(args)
