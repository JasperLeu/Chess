from graphics import *
import graphics

# MOVE NOTATION ==> a1b2, c7h4, d8g8
# ** GLOBAL VARIABLES **
pieceDict = ["pawn", "knight", "bishop", "rook", "queen", "king"]
board = [[None for _ in range(8)] for _ in range(8)]
toMove = "white"
_selectedSpace = None
_possibleMoves = []

def update():
    global _selectedSpace
    global _possibleMoves
    press = refresh(board, _possibleMoves)
    if press is not None:
        _selectedSpace = board[press[0]][press[1]]
        _possibleMoves = _selectedSpace.getMoves()
    
def flipBoard():
    graphics.FLIPPED = not graphics.FLIPPED
    graphics.drawBoard()
    
# Initialize Board
def init():
    graphics.drawBoard()
    for x in range(8):
        for y in range(8):
            if y == 1 or y == 6:
                board[x][y] = Piece("black" if y == 6 else "white", x, y, "pawn")
            elif y == 0 or y == 7:
                p = ""
                if x == 0 or x == 7: p = "rook"
                if x == 1 or x == 6: p = "knight"
                if x == 2 or x == 5: p = "bishop"
                if x == 3: p = "queen"
                if x == 4: p = "king"
                board[x][y] = Piece("black" if y == 7 else "white", x, y, p)
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
            moves += [[0, 1] if self.side == "white" else [0, -1]]
            if self.side == "white" and self.y == 1 or self.side == "black" and self.y == 6:
                moves += [[0, 2] if self.side == "white" else [0, -2]]
        elif self.piece == "knight":
            for x in [-1, 1]:
                for y in [-1, 1]:
                    moves += [[2*x, y], [x, 2*y]]
        elif self.piece == "bishop":
            for i in range(1, 8):
                for x in [-1, 1]:
                    for y in [-1, 1]:
                        moves.append([i*x, i*y])
        elif self.piece == "rook":
            for i in range(1, 8):
                for sign in [-1, 1]:
                    moves += [[i * sign, 0], [0, i * sign]]
        elif self.piece == "queen":
            for i in range(1, 8):
                for x in [-1, 1]:
                    for y in [-1, 1]:
                        moves.append([i*x, i*y])
                    moves += [[i * x, 0], [0, i * x]]
        elif self.piece == "king":
            for x in [-1, 0, 1]:
                for y in [-1, 0, 1]:
                    if not x == 0 or not y == 0:
                        moves.append([x, y])

        final_moves = []
        for m in moves:
            m[0] += self.x
            m[1] += self.y
            if 0 <= m[0] <= 7 and 0 <= m[1] <= 7:
                final_moves.append(m)

        return final_moves
