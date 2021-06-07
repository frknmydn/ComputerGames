import pygame


class Level(object):
    def __init__(self, player):
        super().__init__()
        self.ladder_list = pygame.sprite.Group()
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.coin_list = pygame.sprite.Group()
        self.player = player
        self.coinAmount = 0

    def update(self):
        self.ladder_list.update(())
        self.platform_list.update()
        self.enemy_list.update()

    def draw(self, screen):
        self.ladder_list.draw(screen)
        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)