from multiprocessing import Process


class Component(object):

    def __init__(self, pins, name=None):
        super(Component, self).__init__()
        self.pins = pins
        self.name = name
        if not self.name:
            self.name = self.__class__.__name__

        self.process = None

    def _on(self):
        raise NotImplementedError

    def _off(self):
        raise NotImplementedError

    def on(self):
        print "turning on {}".format(self)
        self.process = Process(target=self._on)
        self.process.start()

    def off(self):
        print "turning off {}".format(self)
        if self.process:
            self.process.terminate()
        self._off()

    def __repr__(self):
        return "<{}(pins={}>".format(self.name, self.pins)
