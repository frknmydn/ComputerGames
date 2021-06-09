import pygame
import random


class Ladder(pygame.sprite.Sprite):
    def __init__(self, x, y, tile_size):
        pygame.sprite.Sprite.__init__(self)
        ladderAsset = pygame.image.load('Assets\Ladders\ladder.png')
        super().__init__()
        self.image = pygame.transform.scale(ladderAsset, (tile_size, tile_size))
        self.rect = self.image.get_rect()
        self.rect.x = x * tile_size
        self.rect.y = y * tile_size
