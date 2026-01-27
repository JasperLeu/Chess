import pygame
from pygame import *

SCREEN_SIZE = 400
SPACE_SIZE = SCREEN_SIZE/8
BOARD_COLORS = [(240, 240, 240), (100, 90, 80)]
running = True

pygame.init()
screen = display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
bgSurf = Surface(screen.get_size(), pygame.SRCALPHA)
piecesSurf = Surface(screen.get_size(), pygame.SRCALPHA)
piecesSheet = pygame.image.load("Pieces.png").convert_alpha()
piecesSheet = pygame.transform.scale(piecesSheet, (SPACE_SIZE*6, SPACE_SIZE*2))
# Create board
for x in range(8):
    for y in range(8):
        draw.rect(bgSurf, BOARD_COLORS[(x+y)%2], (x*SCREEN_SIZE/8, y*SCREEN_SIZE/8, SCREEN_SIZE/8, SCREEN_SIZE/8))

def refresh(board):
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
    piecesSurf.fill((0, 0, 0, 0))
    # add each piece to surface
    pieceSize = piecesSheet.get_height()/2
    for x, r in enumerate(board):
        for y, p in enumerate(r):
            if p == None: continue
            startY = 0 if p.side == 1 else pieceSize
            startX = 0
            if p.piece == "pawn": startX = pieceSize*5
            if p.piece == "knight": startX = pieceSize*3
            if p.piece == "bishop": startX = pieceSize*2
            if p.piece == "rook": startX = pieceSize*4
            if p.piece == "queen": startX = pieceSize
            if p.piece == "king": startX = 0
            newImg = piecesSheet.subsurface(startX, startY, pieceSize, pieceSize)
            piecesSurf.blit(newImg, (x*SPACE_SIZE, y*SPACE_SIZE))
        
    # layer different elements
    screen.blit(bgSurf, (0, 0))
    screen.blit(piecesSurf, (0, 0))
    pygame.display.flip()
