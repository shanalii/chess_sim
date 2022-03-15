# Classes that describe a chess piece with its current position (x,y)

import config


class ChessPiece:
    # get the starting position of the piece in (row, col) coordinates by translating the input string in file notation
    def __init__(self, position_str):
        self.position = config.COLUMN_MAP[position_str[0]], int(position_str[1])

    # get the current position of the piece with file notation (chess format with the letter denoting row)
    def get_file_position(self):
        return config.COLUMN_MAP_REV[self.position[0]] + str(self.position[1] + 1)


class Bishop(ChessPiece):
    def __init__(self, position):
        super().__init__(position)

class Rook(ChessPiece):
    def __init__(self, position):
        super().__init__(position)

    # adjust the piece position after moving - coin = 1: move across rows, coin = 0: move across cols
    def move_piece(self, coin_value, dice_value):
        if coin_value:
            self.position = (self.position[0] - dice_value) % config.BOARD_LENGTH, self.position[1]
        else:
            self.position = self.position[0], (self.position[1] + dice_value) % config.BOARD_LENGTH
            
