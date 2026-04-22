import pygame
from pygame import *

FLIPPED = False
pygame.init()

class Window:
    def __init__(self, width, height, num_layers, scaleFac=1):
        self.screen = display.set_mode((width, height))
        self.layers = [Surface(self.screen.get_size(), pygame.SRCALPHA)]
        self.scale = scaleFac
        self.PIECE_SHEET = pygame.image.load("Pieces.png").convert_alpha()
        self.PIECE_SHEET = pygame.transform.scale(self.PIECE_SHEET, (scaleFac * 6, scaleFac * 2))
        for i in range(num_layers-1):
            self.layers.append(Surface(self.screen.get_size(), pygame.SRCALPHA))

    def clear(self, toClear):
        for i in toClear:
            self.layers[i].fill((0, 0, 0, 0))

    def updateScreen(self):
        for layer in self.layers:
            self.screen.blit(layer, (0, 0))
        pygame.display.flip()

    def rect(self, surf, c, x, y, w=1, h=1):
        if not FLIPPED:
            draw.rect(surf, c, (x*self.scale, self.screen.get_height()-(y+1)*self.scale, w*self.scale, h*self.scale))
        else:
            draw.rect(surf, c, (x*self.scale, y*self.scale, w*self.scale, h*self.scale))
