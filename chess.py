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
        if type(_selectedSpace) is Piece:
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
        self._moves = []

    def getMoves(self):
        self._moves = []
        if self.piece == "pawn":
            side = 1 if self.side == "white" else -1
            if self.addMove(0, side, 0) == 0:
                self.addMove(0, side*2, 0)
            self.addMove(1, side, 1)
            self.addMove(-1, side, 1)
        elif self.piece == "knight":
            for x in [-1, 1]:
                for y in [-1, 1]:
                    self.addMove(x*2, y)
                    self.addMove(x, y*2)
        elif self.piece == "bishop":
            for x in [-1, 1]:
                for y in [-1, 1]:
                    for i in range(1, 8):
                        if self.addMove(x*i, y*i) != 0:
                            break
        elif self.piece == "rook":
            for sign in [-1, 1]:
                for i in range(1, 8):
                    if self.addMove(i * sign, 0) != 0:
                        break
                for i in range(1, 8):
                    if self.addMove(0, i * sign) != 0:
                        break
        elif self.piece == "queen":
            for x in [-1, 1]:
                for y in [-1, 1]:
                    for i in range(1, 8):
                        if self.addMove(x*i, y*i) != 0:
                            break
                for i in range(1, 8):
                    if self.addMove(i * x, 0) != 0:
                        break
                for i in range(1, 8):
                    if self.addMove(0, i * x) != 0:
                        break
        elif self.piece == "king":
            for x in [-1, 0, 1]:
                for y in [-1, 0, 1]:
                    self.addMove(x, y)
        return self._moves

    # returns -1 for end, 0 for empty, and 1 for taking
    def addMove(self, x, y, req=None):
        x += self.x
        y += self.y
        r = 0
        if x > 7 or x < 0 or y > 7 or y < 0:
            r = -1
        elif board[x][y] == None:
            r = 0
        elif board[x][y].side == self.side:
            r = -1
        else:
            r = 1
        if (req is None or req == r) and r >= 0 and (x != self.x or y != self.y):
            self._moves.append([x, y])
            print(x, y)
        return r