import time


autodelay = 200


class KeyDefinition(object):

    # modifier = HID modifier keycode,
    # keycode = unshifted keycode,
    # shift_keycode = shifted keycode (base),
    # fn_keycode = function keycode
    # cancel_shift / unshift = remove the shift modifier but use the shifted
    # keycode,
    # invert_shift is a special case that inverts the shift modifier
    def __init__(
        self,
        key_id,
        grid_a,
        grid_b,
        modifier=0,
        keycode=None,
        base_string=None,
        shift_keycode=None,
        shift_string=None,
        fn_keycode=None,
        cancel_shift=False,
        invert_shift=False,
        unshift=False,
    ):
        self.key_id = key_id
        self.is_modifier = not modifier == 0
        self.modifier_keycode = modifier
        self.base_keycode = keycode
        self.base_string = base_string
        self.shift_base_keycode = shift_keycode
        self.shift_string = shift_string
        self.fn_keycode = fn_keycode
        self.output_a = grid_a
        self.input_b = grid_b
        self.cancel_shift = cancel_shift
        self.invert_shift = invert_shift
        self.unshift = unshift
        self.state = ""
        self.last_output = 0
        self.with_fn = False

    def __str__(self):
        return f"{self.key_id}({self.state})"

    def timestamp_ms(self):
        return int(time.monotonic_ns() / 1000)

    def matches_grid(self, a, b):
        return self.output_a == a and self.output_b == b

    def matches_id(self, key_id):
        return self.key_id == key_id

    def is_pressed(self):
        return self.state == "PRESSED"

    # mark key as pressed
    # accomodate fn modifier if needed
    #
    # return -1 for normal keypress behaviour
    # return keycode for fn modified keypress

    def press(self, fn: bool) -> int:
        self.state = "PRESSED"
        self.last_output = self.timestamp_ms()
        if fn and self.fn_keycode is not None:
            self.with_fn = True
            return self.fn_keycode
        else:
            self.with_fn = False
            if self.invert_shift or self.unshift or self.cancel_shift:
                return -2
            return -1

    # mark key as held and determine response
    # need to accomodate a change in the fn status
    # need to test autorepeat delay
    #
    # return None for no action
    # return -1 for normal keypress behaviour
    # return keycode for fn modified keypress

    def hold(self, fn: bool) -> int:
        timestamp = self.timestamp_ms()
        # handle change to fn flag only if it changes something
        if not fn == self.with_fn and self.fn_keycode is not None:
            self.with_fn = fn
            self.last_output = timestamp
            if fn:
                return self.fn_keycode
            return -1
        # handle autorepeat delay
        elif autodelay <= timestamp - self.last_output:
            self.last_output = timestamp
            if self.with_fn:
                return self.fn_keycode
            elif self.invert_shift or self.unshift or self.cancel_shift:
                return -3
            else:
                return -1
        return None

    # mark key as released (open)

    def release(self) -> int:
        self.state = "OPEN"
        self.last_output = 0
        self.with_fn = False
        if not self.shift_base_keycode == None:
            return -4
        return 0
