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
from picircuit.components.led import FlashingLED
from RPi import GPIO

def main(args):
    print "start"

    # Causes an LED on pin 12 to flash every 0.1 seconds
    flashing = FlashingLED(pin=12, interval=0.1)

    # Turns on flashing LED, waits for 10 seconds, and turns off LED
    flashing.on()
    time.sleep(10)
    flashing.off()

    print "done"
```

This snippet shows come code to write arbitrary text to LCD1602, which is a popular LCD display commonly used with Arduino and Raspberry Pi

```python
#!/usr/bin/env python
import sys
import time
from picircuit.components.lcd import LCD1602
from RPi import GPIO

def main(args):
    print "start"
    
    # Create an LCD1602 display component
    lcd = LCD1602(rs_pin=12, rw_pin=18)
    lcd.on()

    # Turns on flashing LED, waits for 10 seconds, and turns off LED
    lcd.text("Hello World!")
    time.sleep(10)
    lcd.text("Good Bye!")
    lcd.off()

    print "done"
```
