import pygame
from PlayerClass import Player
from LevelClass import Level
from LadderClass import Ladder
from BulletClass import Bullet
from BrickClass import Brick
from CoinClass import Coin

class World(Level):
    def __init__(self, data, SCREEN_WIDTH, SCREEN_HEIGHT, tile_size, player):
        self.player = player
        Level.__init__(self, player)

        self.tile_list = []
        count_row = 0
        for i in range(1):
            print("xd")
            b = Bullet(1, tile_size, SCREEN_WIDTH, SCREEN_HEIGHT, player)
            b1 = Bullet(2, tile_size, SCREEN_WIDTH, SCREEN_HEIGHT, player)
            b2 = Bullet(3, tile_size, SCREEN_WIDTH, SCREEN_HEIGHT, player)

            self.enemy_list.add(b)
            self.enemy_list.add(b1)
            self.enemy_list.add(b2)
            self.tile_list.append(b)
            self.tile_list.append(b1)
            self.tile_list.append(b2)
        for row in data:

            count_col = 0
            for tile in row:
                if tile == 1:
                    stone = Brick(count_col, count_row, tile_size)
                    self.tile_list.append(stone)
                    self.platform_list.add(stone)
                elif tile == 2:
                    ladder = Ladder(count_col, count_row, tile_size)
                    self.tile_list.append(ladder)
                    self.ladder_list.add(ladder)
                elif tile == 3:
                    coin = Coin(count_col, count_row, tile_size)
                    self.tile_list.append(coin)
                    self.coin_list.add(coin)
                count_col += 1
            count_row += 1

    def draw(self, screen):
        self.coin_list.draw(screen)
        self.platform_list.draw(screen)
        self.ladder_list.draw(screen)
        self.enemy_list.draw(screen)
        # for tile in self.tile_list:
        #   screen.blit(tile)