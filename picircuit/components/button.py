import time
from RPi import GPIO
from picircuit.components.component import Component
from collections import defaultdict

def callback(channel):
    print "fuck {}".format(channel)

class Button(Component):

    def __init__(self, pin):
        super(Button, self).__init__([pin])
        GPIO.setup(self.pins[0], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        self.linked_components = defaultdict(dict)

    def link_component(self, component, mode="toggle", trigger="rising"):
        assert trigger == "rising" or trigger == "falling"
        assert mode == "sticky" or mode == "toggle"
        params = self.linked_components[component]
        params["trigger"] = trigger
        params["mode"] = mode
        params["events"] = []

    def unlink_component(self, component):
        try:
            del self.linked_components[component]
        except KeyError:
            print "warning: trying to unlink component that was never linked"
            pass

    def _on_event(self, channel, event):
        # print "rising {}".format(channel)
        print "{} {}".format(self, event)
        for component, params in self.linked_components.iteritems():
            trigger = params["trigger"]
            mode = params["mode"]
            events = params["events"]

            if mode == "toggle":
                events.append(event)
                # print "events: ", events
                if events == ["rising", "falling"] or events == ["falling", "rising"]:
                    component.toggle()
                    params["events"] = []
                continue

            if mode == "sticky":
                if event == trigger:
                    component.on()
                else:
                    component.off()

    def _on(self):
        # GPIO.add_event_detect(self.pins[0], GPIO.BOTH, callback=callback, bouncetime=30
        # GPIO.add_event_detect(self.pins[0], GPIO.RISING, callback=self._rising, bouncetime=300)
        state = "low"
        while True:
            if (GPIO.input(self.pins[0]) == 1):
                if state == "low":
                    self._on_event(self.pins[0], "rising")
                state = "high"
            else:
                if state == "high":
                    self._on_event(self.pins[0], "falling")
                state = "low"

            time.sleep(0.1)

    def _off(self):
        GPIO.remove_event_detect(self.pins[0])
        self.linked_components = []


