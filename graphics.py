import pygame
from pygame import *

SCREEN_SIZE = 400
SPACE_SIZE = SCREEN_SIZE/8
FLIPPED = False

pygame.init()
screen = display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
layers = [Surface(screen.get_size(), pygame.SRCALPHA)]
def initLayers(count):
    for i in range(count-1):
        layers.append(Surface(screen.get_size(), pygame.SRCALPHA))

def clear(toClear):
    for i in toClear:
        layers[i].fill((0, 0, 0, 0))

def loadLayers():
    for layer in layers:
        screen.blit(layer, (0, 0))
    pygame.display.flip()

def rect(surf, c, x, y, w=1, h=1):
    if not FLIPPED:
        draw.rect(surf, c, (x*SPACE_SIZE, SCREEN_SIZE-(y+1)*SPACE_SIZE, w*SPACE_SIZE, h*SPACE_SIZE))
    else:
        draw.rect(surf, c, (x*SPACE_SIZE, y*SPACE_SIZE, w*SPACE_SIZE, h*SPACE_SIZE))
