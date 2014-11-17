import time
from RPi import GPIO
from components.component import Component


class LED(Component):

    def __init__(self, pin):
        print "initializing LED on pin {}".format(pin)
        super(LED, self).__init__([pin])
        GPIO.setup(self.pins[0], GPIO.OUT)

        self._thread = None
        self._process = None

    def _on(self):
        GPIO.output(self.pins[0], 1)

    def _off(self):
        GPIO.output(self.pins[0], 0)


class FlashingLED(LED):

    def __init__(self, pin, interval):
        super(FlashingLED, self).__init__(pin)
        self._interval = interval
        self._sigkill = False

    def _on(self):
        while True:
            super(FlashingLED, self)._on()
            time.sleep(self._interval)
            super(FlashingLED, self)._off()
            time.sleep(self._interval)
