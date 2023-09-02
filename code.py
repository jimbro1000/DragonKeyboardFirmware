import time
import board
import digitalio
import usb_hid

from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode
from key_layout import layout, Fn
from Key_Definition import KeyDefinition


SLEEP_TIME = 0.002


def scan(inkeys, outkeys):
    result = []
    for row in outkeys:
        row.value = True
        row_result = []
        for column in inkeys:
            row_result.append(column.value)
        result.append(row_result)
        row.value = False
    return result


def compare_scan(current, previous):
    delta = []
    j = 0
    for row in current:
        delta.append([])
        i = 0
        for keys in row:
            result = ""
            if current[j][i]:
                if previous[j][i]:
                    result = "HOLD"
                else:
                    result = "PRESS"
            else:
                if previous[j][i]:
                    result = "RELEASE"
            delta[j].append(result)
            i += 1
        j += 1
    return delta


def report_grid(current, delta):
    for i in range(7):
        result = str(i) + "["
        for j in range(8):
            if current[i][j]:
                result += "1"
            else:
                result += "0"
        result += "] ["
        for j in range(8):
            x = delta[i][j]
            if x == "PRESS":
                result += "1"
            elif x == "HOLD":
                result += "2"
            elif x == "RELEASE":
                result += "3"
            else:
                result += "0"
        result += "]"
        print(result)


def process_delta(keys, keyboard, delta):
    fn = False
    modifiers = []
    for key in keys:
        action = delta[key.output_a][key.input_b]
        if key.is_modifier:
            # handle fn, ctrl and shift
            # print("modifier")
            if key.modifier_keycode == Fn:
                fn = True
            else:
                modifiers.append(key.modifier_keycode)
                key.press(fn)
                send_key(key, keyboard, key.modifier_keycode, [])
        else:
            emit = None
            if action == "PRESS":
                emit = key.press(fn)
            elif action == "HOLD":
                emit = key.hold(fn)
            elif action == "RELEASE":
                emit = key.release()
            if emit is not None:
                send_key(key, keyboard, emit, modifiers)


def send_key(key: KeyDefinition, keyboard: Keyboard, key_code: int, modifier: list):
    if key_code == -1:
        keyboard.press(key.base_keycode)
    elif key_code == 0:
        keyboard.release(key.base_keycode)
    else:
        if Keycode.SHIFT in modifier and key.shift_base_keycode is not None:
            key_code = key.shift_base_keycode
        else:
            key_code = key.base_keycode
        if key.cancel_shift or key.invert_shift or key.unshift:
            if Keycode.SHIFT in modifier:
                if key.cancel_shift or key.unshift:
                    keyboard.release(Keycode.SHIFT)
                    keyboard.press(key_code)
                    keyboard.release(key_code)
                    keyboard.press(Keycode.SHIFT)
                else:
                    keyboard.press(key_code)
            else:
                if key.invert_shift:
                    keyboard.press(Keycode.SHIFT)
                    keyboard.press(key_code)
                    keyboard.release(key_code)
                    keyboard.release(Keycode.SHIFT)
                else:
                    keyboard.press(key_code)


def loop(keys, keyboard, grid_a, grid_b):
    grid_previous = None
    while True:
        grid = scan(grid_a, grid_b)
        delta = grid
        if grid_previous is not None:
            delta = compare_scan(grid, grid_previous)
        report_grid(grid, delta)
        process_delta(keys, keyboard, delta)
        grid_previous = grid
        time.sleep(SLEEP_TIME)


def main():
    keys = layout()
    output_pins = [
        board.GP0,
        board.GP1,
        board.GP2,
        board.GP3,
        board.GP4,
        board.GP5,
        board.GP6,
    ]
    grid_a = []
    input_pins = [
        board.GP7,
        board.GP8,
        board.GP9,
        board.GP10,
        board.GP11,
        board.GP12,
        board.GP13,
        board.GP14,
    ]
    grid_b = []

    for pin in output_pins:
        key = digitalio.DigitalInOut(pin)
        key.direction = digitalio.Direction.OUTPUT
        key.drive_mode = digitalio.DriveMode.PUSH_PULL
        grid_a.append(key)

    for pin in input_pins:
        key = digitalio.DigitalInOut(pin)
        key.direction = digitalio.Direction.INPUT
        key.pull = digitalio.Pull.DOWN
        grid_b.append(key)

    keyboard = Keyboard(usb_hid.devices)
    KeyboardLayoutUS(keyboard)

    print("entering infinite scan loop")

    loop(keys, keyboard, grid_b, grid_a)

    applied = []
    while True:
        modifier = []
        fn = False
        for key in keys:
            keycode = 0
            grid_a[key.output_a].value = True
            result = grid_b[key.input_b].value
            grid_a[key.output_a].value = False
            if result:
                if key.is_modifier:
                    fn = key.modifier_keycode == Fn
                    if not fn:
                        modifier.append(key.modifier_keycode)
                else:
                    print(key.base_keycode)
                    if fn:
                        keycode = key.fn_keycode
                    elif (
                        Keycode.SHIFT in modifier and key.shift_base_keycode is not None
                    ):
                        keycode = key.shift_base_keycode
                    else:
                        keycode = key.base_keycode
                if Keycode.SHIFT in modifier:
                    if key.invert_shift or key.cancel_shift or key.unshift:
                        applied = []
                    else:
                        applied = [Keycode.SHIFT]
                else:
                    if key.invert_shift:
                        applied = [Keycode.SHIFT]

                if Keycode.CONTROL in modifier:
                    applied.append(Keycode.CONTROL)
                if not keycode == 0:
                    applied.append(keycode)
                    for press in applied:
                        keyboard.press(press)
                    keyboard.release_all()
                    applied = []

        time.sleep(SLEEP_TIME)


main()
