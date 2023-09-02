import digitalio


class PinConfig(object):
    def __init__(
        self,
        output_drivemode,
        output_default,
        output_poll,
        input_pull,
        input_detect
    ):
        self.drive_mode = output_drivemode
        self.default = output_default
        self.poll = output_poll
        self.pull = input_pull
        self.detect = input_detect

    def setup_output(self,pins):
        result = []
        for pin in pins:
            key = digitalio.DigitalInOut(pin)
            key.direction = digitalio.Direction.OUTPUT
            key.drive_mode = self.drive_mode
            result.append(key)
        return result

    def setup_input(self,pins):
        result = []
        for pin in pins:
            key = digitalio.DigitalInOut(pin)
            key.direction = digitalio.Direction.INPUT
            key.pull = self.pull
            result.append(key)
        return result
