from graphics import *

# MOVE NOTATION ==> a1b2, c7h4, d8g8

def update():
    refresh(board)

class Piece:
    def __init__(self, side, x, y, piece):
        self.x = x
        self.y = y
        self.side = side
        self.piece = pieceDict[piece] if type(piece) is int else piece

    def getMoves(self):
        moves = []
        if self.piece == "pawn":
            inFront = board[x][y+1] if self.side == 1 else board[x][y-1]
        return moves
        
# ** PIECE DICTIONARY **
pieceDict = ["pawn", "knight", "bishop", "rook", "queen", "king"]
board = [[None for _ in range(8)] for _ in range(8)]

# Initialize Board
for x in range(8):
    for y in range(8):
        if y == 1 or y == 6:
            board[x][y] = Piece(0 if y==6 else 1, x, y, "pawn")
        elif y == 0 or y == 7:
            p = ""
            if x == 0 or x == 7: p = "rook"
            if x == 1 or x == 6: p = "knight"
            if x == 2 or x == 5: p = "bishop"
            if x == 3: p = "queen"
            if x == 4: p = "king"
            board[x][y] = Piece(0 if y==7 else 1, x, y, p)
        else:
            board[x][y] = None
    
