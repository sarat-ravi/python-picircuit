#Getting Started
picircuit is an abstraction to make hardware hacking with Raspberry Pi easy, by providing high-level APIs to interface with electrical components

##Examples
The examples below show the code required to interact with components

###Flashing LED
The following snippet of code starts a flashing led, waits for 10 seconds, and turns off the LED component

```python
#!/usr/bin/env python
import sys
import time
from components.led import LED, FlashingLED
from RPi import GPIO

def setup_board():
    print "setting up board"
    GPIO.setmode(GPIO.BOARD)

def main(args):
    print "start"
    setup_board()

    # Causes an LED on pin 12 to flash every 0.1 seconds
    flashing = FlashingLED(pin=12, interval=0.1)

    flashing.on()
    time.sleep(10)
    flashing.off()

    print "done"
```
