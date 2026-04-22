from graphics import *

# ------------------------------------------------------------------------------------------- Initialize Pygame Graphics
SCREEN_SIZE = 400
SPACE_SIZE = SCREEN_SIZE/8
BOARD_COLORS = [(240, 240, 240), (100, 90, 80)]
HIGHLIGHT_COLOR = (150, 230, 245, 150)


# ----------------------------------------------------------------------------------------------------------- GAME CLASS
class Game:
    def __init__(self, showBoard=True):
        self.showBoard = showBoard
        self.board = Board()
        self.turn = "white"
        self.highlighted_squares = []
        self.selectedPiece = []
        if showBoard:
            self.graphic = Window(SCREEN_SIZE, SCREEN_SIZE, 3, SPACE_SIZE)
            for x in range(8):
                for y in range(8):
                    self.graphic.rect(self.graphic.layers[0], BOARD_COLORS[(x + y + 1) % 2], x, y)

    def refresh(self):
        pressPos = None  # Getting pressed square if any
        hasQuit = False
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                hasQuit = True
            elif e.type == pygame.MOUSEBUTTONDOWN:
                pressPos = [0, 0]
                pressPos[0] = int(pygame.mouse.get_pos()[0] // SPACE_SIZE)
                pressPos[1] = int(pygame.mouse.get_pos()[1] // SPACE_SIZE)
                if not FLIPPED:
                    pressPos[1] = 7 - pressPos[1]
        if pressPos is not None:
            if pressPos in self.highlighted_squares:
                self.board.pieces[pressPos[0]][pressPos[1]] = self.board.pieces[self.selectedPiece[0]][self.selectedPiece[1]]
                self.board.pieces[self.selectedPiece[0]][self.selectedPiece[1]] = []
            self.selectedPiece = pressPos
            self.highlighted_squares = self.board.getMovesAtPos(pressPos[0], pressPos[1])

        # Display graphics if specified
        if self.showBoard:
            self.graphic.clear([1, 2])  # clear surfaces
            for move in self.highlighted_squares:
                self.graphic.rect(self.graphic.layers[2], HIGHLIGHT_COLOR, move[0], move[1])
            self.board.display(self.graphic)
            self.graphic.updateScreen()

        return hasQuit


# ---------------------------------------------------------------------------------------------------------- BOARD CLASS
class Board:
    def __init__(self):
        self.pieces = [[[] for i in range(8)] for i in range(8)]
        for x in range(8):
            for y in range(8):
                if y == 1 or y == 6:
                    self.pieces[x][y] = ["black" if y == 6 else "white", "pawn"]
                elif y == 0 or y == 7:
                    p = ""
                    if x == 0 or x == 7: p = "rook"
                    if x == 1 or x == 6: p = "knight"
                    if x == 2 or x == 5: p = "bishop"
                    if x == 3: p = "queen"
                    if x == 4: p = "king"
                    self.pieces[x][y] = ["black" if y == 7 else "white", p]
                else:
                    self.pieces[x][y] = []

    def display(self, graphic):
        # add each piece to surface
        pieceSize = graphic.PIECE_SHEET.get_height() / 2
        for x, r in enumerate(self.pieces):
            for y, p in enumerate(r):
                if len(p) == 0:
                    continue
                side = p[0]
                piece = p[1]
                startY = 0 if side == "white" else pieceSize
                startX = 0
                if piece == "pawn": startX = pieceSize * 5
                if piece == "knight": startX = pieceSize * 3
                if piece == "bishop": startX = pieceSize * 2
                if piece == "rook": startX = pieceSize * 4
                if piece == "queen": startX = pieceSize
                if piece == "king": startX = 0
                newImg = graphic.PIECE_SHEET.subsurface(startX, startY, pieceSize, pieceSize)
                if FLIPPED:
                    graphic.layers[1].blit(newImg, (x * SPACE_SIZE, y * SPACE_SIZE))
                else:
                    graphic.layers[1].blit(newImg, (x * SPACE_SIZE, SCREEN_SIZE - (y + 1) * SPACE_SIZE))

    def getMovesAtPos(self, x, y):
        if len(self.pieces[x][y]) == 0:
            return []
        moves = []
        side, piece = self.pieces[x][y]
        if piece == "pawn":
            s = 1 if side == "white" else -1
            if self.addMove(moves, x, y, 0, s, 0) == 0 and y == int(3.5 - 2.5 * s):
                self.addMove(moves, x, y, 0, s*2)
            self.addMove(moves, x, y, -1, s, 1)
            self.addMove(moves, x, y, 1, s, 1)
        elif piece == "knight":
            for x1 in [-1, 1]:
                for y1 in [-1, 1]:
                    self.addMove(moves, x, y, x1 * 2, y1)
                    self.addMove(moves, x, y, x1, y1 * 2)
        elif piece == "bishop":
            for x1 in [-1, 1]:
                for y1 in [-1, 1]:
                    for i in range(1, 8):
                        if self.addMove(moves, x, y, x1 * i, y1 * i) != 0:
                            break
        elif piece == "rook":
            for sign in [-1, 1]:
                for i in range(1, 8):
                    if self.addMove(moves, x, y, i * sign, 0) != 0:
                        break
                for i in range(1, 8):
                    if self.addMove(moves, x, y, 0, i * sign) != 0:
                        break
        elif piece == "queen":
            for x1 in [-1, 1]:
                for y1 in [-1, 1]:
                    for i in range(1, 8):
                        if self.addMove(moves, x, y, x1 * i, y1 * i) != 0:
                            break
                for i in range(1, 8):
                    if self.addMove(moves, x, y, i * x1, 0) != 0:
                        break
                for i in range(1, 8):
                    if self.addMove(moves, x, y, 0, i * x1) != 0:
                        break
        else:
            for x1 in [-1, 0, 1]:
                for y1 in [-1, 0, 1]:
                    self.addMove(moves, x, y, x1, y1)
        return moves

    # returns -1 for end, 0 for empty, and 1 for taking
    def addMove(self, moveList, x, y, moveX, moveY, req=None):
        moveX += x
        moveY += y
        r = 0
        if moveX > 7 or moveX < 0 or moveY > 7 or moveY < 0:
            r = -1
        elif len(self.pieces[moveX][moveY]) == 0:
            r = 0
        elif self.pieces[moveX][moveY][0] == self.pieces[x][y][0]:
            r = -1
        else:
            r = 1
        if (req is None or req == r) and r >= 0 and (moveX != x or moveY != y):
            moveList.append([moveX, moveY])
        return r
