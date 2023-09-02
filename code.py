import time
import board
import digitalio
import usb_hid
# import supervisor

from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode
from key_layout import simple_layout, Fn
from Key_Definition import KeyDefinition
from Pin_Config import PinConfig


SLEEP_TIME = 0.002
PRESS = 1
HOLD = 2
RELEASE = 3
OPEN = 0


def scan(inkeys, outkeys, config):
    result = []
    for row in outkeys:
        row.value = config.poll
        row_result = []
        for column in inkeys:
            row_result.append(column.value == config.detect)
        result.append(row_result)
        row.value = config.default
    return result


def compare_scan(current, previous):
    delta = []
    j = 0
    for row in current:
        delta.append([])
        i = 0
        for keys in row:
            result = OPEN
            if current[j][i]:
                if previous[j][i]:
                    result = HOLD
                else:
                    result = PRESS
            else:
                if previous[j][i]:
                    result = RELEASE
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
            if x == PRESS:
                result += "1"
            elif x == HOLD:
                result += "2"
            elif x == RELEASE:
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
            if key.modifier_keycode == Fn:
                fn = action == PRESS or action == HOLD
            else:
                if action == PRESS:
                    modifiers.append(key.modifier_keycode)
                    key.press(fn)
                    keyboard.press(key.modifier_keycode)
                elif action == HOLD:
                    modifiers.append(key.modifier_keycode)
                elif action == RELEASE:
                    key.release()
                    keyboard.release(key.modifier_keycode)
        else:
            emit = None
            if action == PRESS:
                emit = key.press(fn)
            elif action == HOLD:
                emit = key.hold(fn)
            elif action == RELEASE:
                emit = key.release()
            if emit is not None:
                emit_key(key, keyboard, emit)


def emit_key(key: KeyDefinition, keyboard: Keyboard, key_code: int):
    if key_code == -1:
        keyboard.press(key.base_keycode)
    elif key_code == 0:
        keyboard.release(key.base_keycode)
    else:
        print("shouldn't get here")


def send_key(key: KeyDefinition, keyboard: Keyboard, key_code: int, modifier: list):
    if key_code == -1:
        keyboard.press(key.base_keycode)
        print("press " + key.key_id)
    elif key_code == 0:
        keyboard.release(key.base_keycode)
        print("release " + key.key_id)
    elif key_code == -3:
        # nop
        print("fake release " + key.key_id)
    elif key_code == -4:
        keyboard.release(key.shift_base_keycode)
    else:
        if Keycode.SHIFT in modifier:
            if key.shift_base_keycode is not None:
                key_code = key.shift_base_keycode
            else:
                key_code = key.base_keycode
            print("shift " + key.key_id)
        else:
            key_code = key.base_keycode
            print("noshift " + key.key_id)

        if key.cancel_shift or key.invert_shift or key.unshift:
            if Keycode.SHIFT in modifier:
                if key.cancel_shift or key.unshift:
                    keyboard.release(Keycode.SHIFT)
                    keyboard.press(key_code)
                    keyboard.release(key_code)
                    keyboard.press(Keycode.SHIFT)
                else:
                    keyboard.press(key_code)
                    keyboard.release(key_code)
            else:
                if key.invert_shift:
                    keyboard.press(Keycode.SHIFT)
                    keyboard.press(key_code)
                    keyboard.release(key_code)
                    keyboard.release(Keycode.SHIFT)
                else:
                    keyboard.press(key_code)
                    keyboard.release(key_code)


def loop(keys, config, keyboard, grid_a, grid_b):
    grid_previous = None
    while True:
        grid = scan(grid_a, grid_b, config)
        delta = grid
        if grid_previous is not None:
            delta = compare_scan(grid, grid_previous)
        # report_grid(grid, delta)
        process_delta(keys, keyboard, delta)
        grid_previous = grid
        time.sleep(SLEEP_TIME)


def main():
    keys = simple_layout()
    use_config = PinConfig(
        digitalio.DriveMode.PUSH_PULL, True, False, digitalio.Pull.UP, False
    )

    output_pins = [
        board.GP0,
        board.GP1,
        board.GP2,
        board.GP3,
        board.GP4,
        board.GP5,
        board.GP6,
    ]
    grid_a = use_config.setup_output(output_pins)
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
    grid_b = use_config.setup_input(input_pins)

    keyboard = Keyboard(usb_hid.devices)
    KeyboardLayoutUS(keyboard)

    print("entering infinite scan loop")

    loop(keys, use_config, keyboard, grid_b, grid_a)

# supervisor.runtime.autoreload = False
main()
