# NOTE: I will try to migrate to qmk soon.

print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys

keyboard = KMKKeyboard()

keyboard.col_pins = (board.GP26, board.GP27, board.GP28, board.GP29)
keyboard.row_pins = (board.GP3, board.GP4, board.GP2, board.GP1)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

encoder = EncoderHandler()
encoder.pins = (
    (board.GP7, board.GP6, None),  
)
encoder.map = [
    ((KC.VOLD, KC.VOLU, KC.NO),),  
]
keyboard.modules.append(encoder)
keyboard.extensions.append(MediaKeys())

keyboard.keymap = [
    [
        KC.N1, KC.N2, KC.N3, KC.MUTE,   
        KC.N4, KC.N5, KC.N6, KC.N7,     
        KC.N8, KC.N9, KC.N0, KC.ENT,    
        KC.A,  KC.B,  KC.C,  KC.D,      
    ],
]

if __name__ == "__main__":
    keyboard.go()
