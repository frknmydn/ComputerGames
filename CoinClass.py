import pygame


class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y, tile_size):
        pygame.sprite.Sprite.__init__(self)
        coinAsset = pygame.image.load('Assets\Coin\spriteCoin.png')
        super().__init__()
        self.image = pygame.transform.scale(coinAsset, (round(tile_size / 2), round(tile_size / 2)))
        self.rect = self.image.get_rect()
        self.rect.x = round((x + 0.2) * tile_size)
        self.rect.y = round((y + 0.2) * tile_size)