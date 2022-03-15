# Class that represents a chessboard, with 2 pieces, a rook and a bishop. Also handles coin flipping, dice rolling, and
# moving the pieces.

import config
import random

from pieces import Bishop, Rook


class Chessboard:
    def __init__(self, bishop_pos, rook_pos):
        self.board = [["o" for _ in range(config.BOARD_LENGTH)] for _ in range(config.BOARD_LENGTH)]
        self.bishop = Bishop(bishop_pos)
        self.rook = Rook(rook_pos)
        print("Starting board:")
        self.get_board_state()

    def _flip_coin(self):
        result = random.randrange(2)
        if result:
            print("Coin flipped heads, rook moves up")
        else:
            print("Coin flipped tails, rook moves right")
        return result

    def _roll_dice(self):
        result = 0
        for i in range(config.NUM_DICE):
            result += random.randrange(1, config.DICE_FACES + 1)
        print("Dice rolled", str(result))
        return result

    # refresh and print the board state after pieces have moved
    def get_board_state(self):
        self.board[self.bishop.position[0]][self.bishop.position[1]] = "B"
        self.board[self.rook.position[0]][self.rook.position[1]] = "R"

        for i in range(config.BOARD_LENGTH):
            row = ""
            for j in range(config.BOARD_LENGTH):
                row += str(self.board[i][j])
            print(row)

        print("Rook at " + self.rook.get_file_position())
        print("Bishop at " + self.bishop.get_file_position())
        print()

    # move the rook by calling rook.get_path(), wrap the path around the board and check if the bishop is in the way
    # return whether or not the bishop has been eaten
    def move_rook(self):
        coin_value = self._flip_coin()
        dice_value = self._roll_dice()
        taken = False

        bishop_y, bishop_x = self.bishop.position[0], self.bishop.position[1]
        rook_y, rook_x = self.rook.position[0], self.rook.position[1]

        # remove the rook from the board since it is moving
        self.board[rook_y][rook_x] = "o"

        # to check if rook takes bishop:
        # case 1: if bishop is in front of rook at first, and then rook gets in front of bishop after moving
        # case 2: if bishop is behind rook at first, and then rook gets in front of bishop after wrapping around board

        # if the rook moves vertically and the bishop is on the same col
        if coin_value and bishop_x == rook_x:
            if (rook_y > bishop_y >= (rook_y - dice_value)) or \
                    (bishop_y > rook_y and rook_y + dice_value >= config.BOARD_LENGTH
                     and (rook_y - dice_value) % config.BOARD_LENGTH <= bishop_y):
                taken = True

        # if the rook moves horizontally and the bishop is on the same row
        elif not coin_value and bishop_y == rook_y:
            if (rook_x < bishop_x <= (rook_x + dice_value)) or \
                    (bishop_x < rook_x and rook_x + dice_value >= config.BOARD_LENGTH
                     and (rook_x + dice_value) % config.BOARD_LENGTH >= bishop_x):
                taken = True

        # finally update the rook position
        self.rook.move_piece(coin_value, dice_value)
        self.get_board_state()
        return taken
      
