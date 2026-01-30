from graphics import *
import graphics

# MOVE NOTATION ==> a1b2, c7h4, d8g8
# ** GLOBAL VARIABLES **
pieceDict = ["pawn", "knight", "bishop", "rook", "queen", "king"]
board = [[None for _ in range(8)] for _ in range(8)]
toMove = "white"
_selectedSpace = None

def update():
    global _selectedSpace
    moves = []
    if not _selectedSpace is None:
        moves = _selectedSpace.getMoves()
    press = refresh(board, moves)
    if not press is None:
        _selectedSpace = board[press[0]][press[1]]
    
def flipBoard():
    graphics.FLIPPED = not graphics.FLIPPED
    graphics.drawBoard()
    
# Initialize Board
def init():
    graphics.drawBoard()
    for x in range(8):
        for y in range(8):
            if y == 1 or y == 6:
                board[x][y] = Piece("black" if y==6 else "white", x, y, "pawn")
            elif y == 0 or y == 7:
                p = ""
                if x == 0 or x == 7: p = "rook"
                if x == 1 or x == 6: p = "knight"
                if x == 2 or x == 5: p = "bishop"
                if x == 3: p = "queen"
                if x == 4: p = "king"
                board[x][y] = Piece("black" if y==7 else "white", x, y, p)
            else:
                board[x][y] = None

class Piece:
    def __init__(self, side, x, y, piece):
        self.x = x
        self.y = y
        self.side = side
        self.piece = pieceDict[piece] if type(piece) is int else piece

    def getMoves(self):
        moves = []
        if self.piece == "pawn":
            moves += [[self.x, self.y+1] if self.side == "white" else [self.x, self.y-1]]
            if self.side == "white" and self.y == 1 or self.side == "black" and self.y == 6:
                moves+=[[self.x, self.y+2] if self.side == "white" else [self.x, self.y-2]]
        if self.piece == "knight":
            for s in [-1, 1]
                
        for m in moves:
            if m[0] < 0 or m[1] > 7 or m[1] < 0 or m[1] > 7:
                moves.remove(m)
        return moves
