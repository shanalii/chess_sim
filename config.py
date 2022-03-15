# Config file to store the final variables and their values.

BOARD_LENGTH = 8
NUM_TURNS = 15
DICE_FACES = 6
NUM_DICE = 1
COLUMN_MAP = {
    "a": 0,
    "b": 1,
    "c": 2,
    "d": 3,
    "e": 4,
    "f": 5,
    "g": 6,
    "h": 7
}
COLUMN_MAP_REV = {v: k for k, v in COLUMN_MAP.items()}
BISHOP_START = "c3"
ROOK_START = "h1"
