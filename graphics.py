import pygame
import cv2
from pygame import *

SCREEN_SIZE = 500
BOARD_COLORS = [(240, 240, 240), (100, 90, 80)]
piecesSheet = cv2.imread("Pieces.png")
running = True

pygame.init()
screen = display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
bgSurf = Surface(screen.get_size(), pygame.SRCALPHA)
piecesSurf = Surface(screen.get_size(), pygame.SRCALPHA)

# Create board
for x in range(8):
    for y in range(8):
        draw.rect(bgSurf, BOARD_COLORS[(x+y)%2], (x*SCREEN_SIZE/8, y*SCREEN_SIZE/8, SCREEN_SIZE/8, SCREEN_SIZE/8))

def refresh(pieces):
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
    piecesSurf.fill((0, 0, 0, 0))
    # add each piece to surface
    pieceSize = piecesSheet.size/6
    for p in pieces:
        if p.piece == 1:
            # img = piecesSheet[-pieceSize:][]
            continue

    # layer different elements
    screen.blit(bgSurf, (0, 0))
    screen.blit(piecesSurf, (0, 0))
    pygame.display.flip()