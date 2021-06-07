import pygame
import random

class Ladder(pygame.sprite.Sprite):
    def __init__(self, x, y, tile_size):
        pygame.sprite.Sprite.__init__(self)
        super().__init__()
        self.image = pygame.Surface((tile_size, tile_size))
        self.image.fill(pygame.Color("blue"))
        self.rect = self.image.get_rect()
        self.rect.x = x * tile_size
        self.rect.y = y * tile_size