from adafruit_hid.keycode import Keycode
from Key_Definition import KeyDefinition


Fn = -1


def simple_layout():
    keyset = [
        KeyDefinition(key_id="shift", modifier=Keycode.SHIFT, grid_a=6, grid_b=7),
        KeyDefinition(key_id="ctrl", modifier=Keycode.CONTROL, grid_a=6, grid_b=3),
        KeyDefinition(key_id="fn", modifier=Fn, grid_a=6, grid_b=6),
        KeyDefinition(
            key_id="0",
            keycode=Keycode.ZERO,
            fn_keycode=Keycode.F10,
            grid_a=0,
            grid_b=0,
        ),
        KeyDefinition(
            key_id="1", keycode=Keycode.ONE, fn_keycode=Keycode.F1, grid_a=0, grid_b=1
        ),
        KeyDefinition(
            key_id="2",
            keycode=Keycode.TWO,
            fn_keycode=Keycode.F2,
            grid_a=0,
            grid_b=2,
        ),
        KeyDefinition(
            key_id="3", keycode=Keycode.THREE, fn_keycode=Keycode.F3, grid_a=0, grid_b=3
        ),
        KeyDefinition(
            key_id="4", keycode=Keycode.FOUR, fn_keycode=Keycode.F4, grid_a=0, grid_b=4
        ),
        KeyDefinition(
            key_id="5", keycode=Keycode.FIVE, fn_keycode=Keycode.F5, grid_a=0, grid_b=5
        ),
        KeyDefinition(
            key_id="6", keycode=Keycode.SIX, fn_keycode=Keycode.F6, grid_a=0, grid_b=6
        ),
        KeyDefinition(
            key_id="7",
            keycode=Keycode.SEVEN,
            fn_keycode=Keycode.F7,
            grid_a=0,
            grid_b=7,
        ),
        KeyDefinition(
            key_id="8",
            keycode=Keycode.EIGHT,
            fn_keycode=Keycode.F8,
            grid_a=1,
            grid_b=0,
        ),
        KeyDefinition(
            key_id="9",
            keycode=Keycode.NINE,
            fn_keycode=Keycode.F9,
            grid_a=1,
            grid_b=1,
        ),
        KeyDefinition(
            key_id=":",
            keycode=Keycode.MINUS,
            fn_keycode=Keycode.F11,
            grid_a=1,
            grid_b=2,
        ),
        KeyDefinition(
            key_id=";",
            keycode=Keycode.SEMICOLON,
            grid_a=1,
            grid_b=3,
        ),
        KeyDefinition(key_id=",", keycode=Keycode.COMMA, grid_a=1, grid_b=4),
        KeyDefinition(
            key_id="-",
            keycode=Keycode.EQUALS,
            fn_keycode=Keycode.F12,
            grid_a=1,
            grid_b=5,
        ),
        KeyDefinition(key_id=".", keycode=Keycode.PERIOD, grid_a=1, grid_b=6),
        KeyDefinition(
            key_id="slash", keycode=Keycode.FORWARD_SLASH, grid_a=1, grid_b=7
        ),
        KeyDefinition(
            key_id="at",
            keycode=Keycode.LEFT_BRACKET,
            grid_a=2,
            grid_b=0,
        ),
        KeyDefinition(key_id="a", keycode=Keycode.A, grid_a=2, grid_b=1),
        KeyDefinition(key_id="b", keycode=Keycode.B, grid_a=2, grid_b=2),
        KeyDefinition(key_id="c", keycode=Keycode.C, grid_a=2, grid_b=3),
        KeyDefinition(key_id="d", keycode=Keycode.D, grid_a=2, grid_b=4),
        KeyDefinition(key_id="e", keycode=Keycode.E, grid_a=2, grid_b=5),
        KeyDefinition(key_id="f", keycode=Keycode.F, grid_a=2, grid_b=6),
        KeyDefinition(key_id="g", keycode=Keycode.G, grid_a=2, grid_b=7),
        KeyDefinition(key_id="h", keycode=Keycode.H, grid_a=3, grid_b=0),
        KeyDefinition(key_id="i", keycode=Keycode.I, grid_a=3, grid_b=1),
        KeyDefinition(key_id="j", keycode=Keycode.J, grid_a=3, grid_b=2),
        KeyDefinition(key_id="k", keycode=Keycode.K, grid_a=3, grid_b=3),
        KeyDefinition(key_id="l", keycode=Keycode.L, grid_a=3, grid_b=4),
        KeyDefinition(key_id="m", keycode=Keycode.M, grid_a=3, grid_b=5),
        KeyDefinition(key_id="n", keycode=Keycode.N, grid_a=3, grid_b=6),
        KeyDefinition(key_id="o", keycode=Keycode.O, grid_a=3, grid_b=7),
        KeyDefinition(key_id="p", keycode=Keycode.P, grid_a=4, grid_b=0),
        KeyDefinition(key_id="q", keycode=Keycode.Q, grid_a=4, grid_b=1),
        KeyDefinition(key_id="r", keycode=Keycode.R, grid_a=4, grid_b=2),
        KeyDefinition(key_id="s", keycode=Keycode.S, grid_a=4, grid_b=3),
        KeyDefinition(key_id="t", keycode=Keycode.T, grid_a=4, grid_b=4),
        KeyDefinition(key_id="u", keycode=Keycode.U, grid_a=4, grid_b=5),
        KeyDefinition(key_id="v", keycode=Keycode.V, grid_a=4, grid_b=6),
        KeyDefinition(key_id="w", keycode=Keycode.W, grid_a=4, grid_b=7),
        KeyDefinition(key_id="x", keycode=Keycode.X, grid_a=5, grid_b=0),
        KeyDefinition(key_id="y", keycode=Keycode.Y, grid_a=5, grid_b=1),
        KeyDefinition(key_id="z", keycode=Keycode.Z, grid_a=5, grid_b=2),
        KeyDefinition(key_id="up", keycode=Keycode.UP_ARROW, grid_a=5, grid_b=3),
        KeyDefinition(key_id="down", keycode=Keycode.DOWN_ARROW, grid_a=5, grid_b=4),
        KeyDefinition(key_id="left", keycode=Keycode.LEFT_ARROW, grid_a=5, grid_b=5),
        KeyDefinition(key_id="right", keycode=Keycode.RIGHT_ARROW, grid_a=5, grid_b=6),
        KeyDefinition(key_id="space", keycode=Keycode.SPACE, grid_a=5, grid_b=7),
        KeyDefinition(key_id="enter", keycode=Keycode.ENTER, grid_a=6, grid_b=0),
        KeyDefinition(key_id="clear", keycode=Keycode.GRAVE_ACCENT, grid_a=6, grid_b=1),
        KeyDefinition(
            key_id="break",
            keycode=Keycode.ESCAPE,
            grid_a=6,
            grid_b=2,
        ),
    ]
    return keyset


def layout():
    # print("initialise keyboard key set")
    keyset = [
        KeyDefinition(key_id="shift", modifier=Keycode.SHIFT, grid_a=6, grid_b=7),
        KeyDefinition(key_id="ctrl", modifier=Keycode.CONTROL, grid_a=6, grid_b=3),
        KeyDefinition(key_id="fn", modifier=Fn, grid_a=6, grid_b=6),
        KeyDefinition(
            key_id="0",
            keycode=Keycode.ZERO,
            cancel_shift=True,
            fn_keycode=Keycode.F10,
            grid_a=0,
            grid_b=0,
        ),
        KeyDefinition(
            key_id="1", keycode=Keycode.ONE, fn_keycode=Keycode.F1, grid_a=0, grid_b=1
        ),
        KeyDefinition(
            key_id="2",
            keycode=Keycode.TWO,
            shift_keycode=Keycode.QUOTE,
            fn_keycode=Keycode.F2,
            grid_a=0,
            grid_b=2,
        ),
        KeyDefinition(
            key_id="3", keycode=Keycode.THREE, fn_keycode=Keycode.F3, grid_a=0, grid_b=3
        ),
        KeyDefinition(
            key_id="4", keycode=Keycode.FOUR, fn_keycode=Keycode.F4, grid_a=0, grid_b=4
        ),
        KeyDefinition(
            key_id="5", keycode=Keycode.FIVE, fn_keycode=Keycode.F5, grid_a=0, grid_b=5
        ),
        KeyDefinition(
            key_id="6", keycode=Keycode.SIX, fn_keycode=Keycode.F6, grid_a=0, grid_b=6
        ),
        KeyDefinition(
            key_id="7",
            keycode=Keycode.SEVEN,
            shift_keycode=Keycode.QUOTE,
            cancel_shift=True,
            fn_keycode=Keycode.F7,
            grid_a=0,
            grid_b=7,
        ),
        KeyDefinition(
            key_id="8",
            keycode=Keycode.EIGHT,
            shift_keycode=Keycode.NINE,
            fn_keycode=Keycode.F8,
            grid_a=1,
            grid_b=0,
        ),
        KeyDefinition(
            key_id="9",
            keycode=Keycode.NINE,
            shift_keycode=Keycode.ZERO,
            fn_keycode=Keycode.F9,
            grid_a=1,
            grid_b=1,
        ),
        KeyDefinition(
            key_id=":",
            keycode=Keycode.SEMICOLON,
            invert_shift=True,
            shift_keycode=Keycode.EIGHT,
            fn_keycode=Keycode.F11,
            grid_a=1,
            grid_b=2,
        ),
        KeyDefinition(
            key_id=";",
            keycode=Keycode.SEMICOLON,
            shift_keycode=Keycode.EQUALS,
            grid_a=1,
            grid_b=3,
        ),
        KeyDefinition(key_id=",", keycode=Keycode.COMMA, grid_a=1, grid_b=4),
        KeyDefinition(
            key_id="-",
            keycode=Keycode.MINUS,
            shift_keycode=Keycode.EQUALS,
            unshift=True,
            fn_keycode=Keycode.F12,
            grid_a=1,
            grid_b=5,
        ),
        KeyDefinition(key_id=".", keycode=Keycode.PERIOD, grid_a=1, grid_b=6),
        KeyDefinition(
            key_id="slash", keycode=Keycode.FORWARD_SLASH, grid_a=1, grid_b=7
        ),
        KeyDefinition(
            key_id="at",
            keycode=Keycode.TWO,
            invert_shift=True,
            cancel_shift=True,
            grid_a=2,
            grid_b=0,
        ),
        KeyDefinition(key_id="a", keycode=Keycode.A, grid_a=2, grid_b=1),
        KeyDefinition(key_id="b", keycode=Keycode.B, grid_a=2, grid_b=2),
        KeyDefinition(key_id="c", keycode=Keycode.C, grid_a=2, grid_b=3),
        KeyDefinition(key_id="d", keycode=Keycode.D, grid_a=2, grid_b=4),
        KeyDefinition(key_id="e", keycode=Keycode.E, grid_a=2, grid_b=5),
        KeyDefinition(key_id="f", keycode=Keycode.F, grid_a=2, grid_b=6),
        KeyDefinition(key_id="g", keycode=Keycode.G, grid_a=2, grid_b=7),
        KeyDefinition(key_id="h", keycode=Keycode.H, grid_a=3, grid_b=0),
        KeyDefinition(key_id="i", keycode=Keycode.I, grid_a=3, grid_b=1),
        KeyDefinition(key_id="j", keycode=Keycode.J, grid_a=3, grid_b=2),
        KeyDefinition(key_id="k", keycode=Keycode.K, grid_a=3, grid_b=3),
        KeyDefinition(key_id="l", keycode=Keycode.L, grid_a=3, grid_b=4),
        KeyDefinition(key_id="m", keycode=Keycode.M, grid_a=3, grid_b=5),
        KeyDefinition(key_id="n", keycode=Keycode.N, grid_a=3, grid_b=6),
        KeyDefinition(key_id="o", keycode=Keycode.O, grid_a=3, grid_b=7),
        KeyDefinition(key_id="p", keycode=Keycode.P, grid_a=4, grid_b=0),
        KeyDefinition(key_id="q", keycode=Keycode.Q, grid_a=4, grid_b=1),
        KeyDefinition(key_id="r", keycode=Keycode.R, grid_a=4, grid_b=2),
        KeyDefinition(key_id="s", keycode=Keycode.S, grid_a=4, grid_b=3),
        KeyDefinition(key_id="t", keycode=Keycode.T, grid_a=4, grid_b=4),
        KeyDefinition(key_id="u", keycode=Keycode.U, grid_a=4, grid_b=5),
        KeyDefinition(key_id="v", keycode=Keycode.V, grid_a=4, grid_b=6),
        KeyDefinition(key_id="w", keycode=Keycode.W, grid_a=4, grid_b=7),
        KeyDefinition(key_id="x", keycode=Keycode.X, grid_a=5, grid_b=0),
        KeyDefinition(key_id="y", keycode=Keycode.Y, grid_a=5, grid_b=1),
        KeyDefinition(key_id="z", keycode=Keycode.Z, grid_a=5, grid_b=2),
        KeyDefinition(key_id="up", keycode=Keycode.UP_ARROW, grid_a=5, grid_b=3),
        KeyDefinition(key_id="down", keycode=Keycode.DOWN_ARROW, grid_a=5, grid_b=4),
        KeyDefinition(key_id="left", keycode=Keycode.LEFT_ARROW, grid_a=5, grid_b=5),
        KeyDefinition(key_id="right", keycode=Keycode.RIGHT_ARROW, grid_a=5, grid_b=6),
        KeyDefinition(key_id="space", keycode=Keycode.SPACE, grid_a=5, grid_b=7),
        KeyDefinition(key_id="enter", keycode=Keycode.ENTER, grid_a=6, grid_b=0),
        KeyDefinition(key_id="clear", keycode=Keycode.GRAVE_ACCENT, grid_a=6, grid_b=1),
        KeyDefinition(
            key_id="break",
            keycode=Keycode.ESCAPE,
            cancel_shift=True,
            grid_a=6,
            grid_b=2,
        ),
    ]
    return keyset
