import time
from RPi import GPIO
from picircuit.components.component import Component
from multiprocessing import Value


class LED(Component):

    def __init__(self, pin):
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
        self._interval = Value('d', interval)

    def _on(self):
        while True:
            super(FlashingLED, self)._on()
            time.sleep(self._interval.value/2.0)
            super(FlashingLED, self)._off()
            time.sleep(self._interval.value/2.0)

    @property
    def interval(self):
        return self._interval.value

    @interval.setter
    def interval(self, interval):
        self._interval.value = interval


