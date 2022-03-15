# Assumptions:
# - Positions of the pieces are given as a string, using the file notation in chess (eg. c1).
# - Certain variables used in the gameplay (eg. number of turns) can be easily changed and scaled up/down, thus stored
# in a config file.
# - The board state is stored in a n^2 array, where n is the length of the board. The rows go top -> bottom (movement
# upwards = decreasing row number), the columns go left -> right (movement rightwards = increasing column number).

import config
from chessboard import Chessboard

if __name__ == '__main__':
    chessboard = Chessboard(config.BISHOP_START, config.ROOK_START)
    taken = False

    for i in range(config.NUM_TURNS):
        print("Turn", str(i + 1))
        if chessboard.move_rook():
            taken = True
            print("Bishop was taken, game ended.")
            break

    if not taken:
        print("Bishop was not taken.")
        
