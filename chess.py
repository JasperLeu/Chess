from graphics import *

# MOVE NOTATION ==> a1b2, c7h4, d8g8

# ** PIECE DICTIONARY **
# 1 - Pawn
# 2 - Knight
# 3 - Bishop
# 4 - Rook
# 5 - Queen
# 6 - King

board = [[]]
pieces = []

def update():
    refresh(pieces)

class Piece:
    def __init__(self, side, x, y, piece):
        self.x = x
        self.y = y
        self.side = side
        self.piece = piece

    def getMoves(self):
        moves = []
        return moves