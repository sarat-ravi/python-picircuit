from multiprocessing import Process


class Component(object):

    def __init__(self, pins, name=None):
        super(Component, self).__init__()
        self.pins = pins
        self.name = name
        if not self.name:
            self.name = self.__class__.__name__

        self.process = None
        pin_name = "pins" if len(self.pins) > 1 else "pin"
        print "created {}, using {} {}".format(self.name, pin_name, ", ".join((str(p) for p in self.pins)))

    def _on(self):
        raise NotImplementedError

    def _off(self):
        raise NotImplementedError

    def is_on(self):
        return not self.process == None

    def toggle(self):
        if self.is_on():
            self.off()
        else:
            self.on()

    def on(self):
        if self.is_on():
            raise Exception("component already on!")
        print "turning on {}".format(self)
        self.process = Process(target=self._on)
        self.process.start()

    def off(self):
        if not self.is_on():
            raise Exception("component already off!")
        print "turning off {}".format(self)
        if self.process:
            self.process.terminate()
        self.process = None
        self._off()

    def __repr__(self):
        return "<{}(pins={}>".format(self.name, self.pins)
