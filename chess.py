from graphics import *
import graphics

# ------------------------------------------------------------------------------------------- Initialize Pygame Graphics
graphics.initLayers(3)
BOARD_COLORS = [(240, 240, 240), (100, 90, 80)]
HIGHLIGHT_COLOR = (150, 230, 245, 150)
PIECE_SHEET = pygame.image.load("Pieces.png").convert_alpha()
PIECE_SHEET = pygame.transform.scale(PIECE_SHEET, (SPACE_SIZE*6, SPACE_SIZE*2))
for x in range(8):
    for y in range(8):
        rect(layers[0], BOARD_COLORS[(x+y+1)%2], x, y)

# ----------------------------------------------------------------------------------------------------------- GAME CLASS
class Game:
    def __init__(self, showBoard=False):
        self.showBoard = showBoard
        self.turn = "white"

# ---------------------------------------------------------------------------------------------------------- BOARD CLASS
class Board:
    def __init__(self):
        self.board = [["" for i in range(8)] for i in range(8)]
        for x in range(8):
            for y in range(8):
                if y == 1 or y == 6:
                    self.board[x][y] = ("black " if y == 6 else "white ") + "pawn"
                elif y == 0 or y == 7:
                    p = ""
                    if x == 0 or x == 7: p = "rook"
                    if x == 1 or x == 6: p = "knight"
                    if x == 2 or x == 5: p = "bishop"
                    if x == 3: p = "queen"
                    if x == 4: p = "king"
                    self.board[x][y] = ("black " if y == 6 else "white ") + p
                else:
                    self.board[x][y] = ""

    def display(self, selectedSpace):
        pressPos = None
        clear([1, 2]) # clear surfaces
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
            elif e.type == pygame.MOUSEBUTTONDOWN:
                pressPos = [0, 0]
                pressPos[0] = int(pygame.mouse.get_pos()[0] // SPACE_SIZE)
                pressPos[1] = int(pygame.mouse.get_pos()[1] // SPACE_SIZE)
                if not FLIPPED:
                    pressPos[1] = 7-pressPos[1]
        # highlight each highlight
        for h in highlights:
            rect(overlaySurf, HIGHLIGHT_COLOR, h[0], h[1])
        # add each piece to surface
        pieceSize = piecesSheet.get_height()/2
        for x, r in enumerate(board):
            for y, p in enumerate(r):
                if p == None: continue
                startY = 0 if p.side == "white" else pieceSize
                startX = 0
                if p.piece == "pawn": startX = pieceSize*5
                if p.piece == "knight": startX = pieceSize*3
                if p.piece == "bishop": startX = pieceSize*2
                if p.piece == "rook": startX = pieceSize*4
                if p.piece == "queen": startX = pieceSize
                if p.piece == "king": startX = 0
                newImg = PIECE_SHEET.subsurface(startX, startY, pieceSize, pieceSize)
                if FLIPPED:
                    layers[1].blit(newImg, (x*SPACE_SIZE, y*SPACE_SIZE))
                else:
                    layers[1].blit(newImg, (x*SPACE_SIZE, SCREEN_SIZE-(y+1)*SPACE_SIZE))
        loadLayers()

# ---------------------------------------------------------------------------------------------------------- PIECE CLASS
class Piece:
    def __init__(self, board, side, x, y, piece):
        self.x = x
        self.y = y
        self.side = side
        self.piece = piece
        self._moves = []
        self.board = board

    def moveTo(self, x, y):
        self.board[self.x][self.y] = None
        self.x = x
        self.y = y
        self.board[x][y] = self

    def getMoves(self):
        self._moves = []
        if self.piece == "pawn":
            side = 1 if self.side == "white" else -1
            if self.addMove(0, side, 0) == 0 and self.y == int(3.5 - 2.5 * side):
                self.addMove(0, side * 2, 0)
            self.addMove(1, side, 1)
            self.addMove(-1, side, 1)
        elif self.piece == "knight":
            for x in [-1, 1]:
                for y in [-1, 1]:
                    self.addMove(x * 2, y)
                    self.addMove(x, y * 2)
        elif self.piece == "bishop":
            for x in [-1, 1]:
                for y in [-1, 1]:
                    for i in range(1, 8):
                        if self.addMove(x * i, y * i) != 0:
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
                        if self.addMove(x * i, y * i) != 0:
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
        elif self.board[x][y] == None:
            r = 0
        elif self.board[x][y].side == self.side:
            r = -1
        else:
            r = 1
        if (req is None or req == r) and r >= 0 and (x != self.x or y != self.y):
            self._moves.append([x, y])
        return r