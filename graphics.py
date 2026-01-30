import pygame
from pygame import *

SCREEN_SIZE = 400
SPACE_SIZE = SCREEN_SIZE/8
BOARD_COLORS = [(240, 240, 240), (100, 90, 80)]
FLIPPED = False
running = True

pygame.init()
screen = display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
bgSurf = Surface(screen.get_size(), pygame.SRCALPHA)
overlaySurf = Surface(screen.get_size(), pygame.SRCALPHA)
piecesSurf = Surface(screen.get_size(), pygame.SRCALPHA)
piecesSheet = pygame.image.load("Pieces.png").convert_alpha()
piecesSheet = pygame.transform.scale(piecesSheet, (SPACE_SIZE*6, SPACE_SIZE*2))
# Create board
def drawBoard():
    for x in range(8):
        for y in range(8):
            rect(bgSurf, BOARD_COLORS[(x+y)%2], x, y)

def refresh(board, highlights):
    pressPos = None
    # clear surfaces
    piecesSurf.fill((0, 0, 0, 0))
    overlaySurf.fill((0, 0, 0, 0))
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
        rect(overlaySurf, (255, 0, 0, 100), h[0], h[1])
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
            newImg = piecesSheet.subsurface(startX, startY, pieceSize, pieceSize)
            if FLIPPED:
                piecesSurf.blit(newImg, (x*SPACE_SIZE, y*SPACE_SIZE))
            else:
                piecesSurf.blit(newImg, (x*SPACE_SIZE, SCREEN_SIZE-(y+1)*SPACE_SIZE))
    # layer different elements
    screen.blit(bgSurf, (0, 0))
    screen.blit(piecesSurf, (0, 0))
    screen.blit(overlaySurf, (0, 0))
    pygame.display.flip()
    
    return pressPos
    
def rect(surf, c, x, y, w=1, h=1):
    if not FLIPPED:
        draw.rect(surf, c, (x*SPACE_SIZE, SCREEN_SIZE-(y+1)*SPACE_SIZE, w*SPACE_SIZE, h*SPACE_SIZE))
    else:
        draw.rect(surf, c, (x*SPACE_SIZE, y*SPACE_SIZE, w*SPACE_SIZE, h*SPACE_SIZE))
