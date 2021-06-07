import pygame
import random

from pygame.locals import *

from LadderClass import Ladder
from PlayerClass import Player
from WorldClass import World


class MainLogic:
    def __init__(self):

        self.fontName = pygame.font.match_font('comicsansms')
        self.game_data = []
        self.SCREEN_WIDTH = 800
        self.SCREEN_HEIGHT = 800
        self.clock = pygame.time.Clock()
        self.FPS = 60
        self.run = True
        self.font = pygame.font.Font(self.fontName, 20)
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.initialScreen = True
        pygame.display.set_caption('Oyun')

        # variables
        self.tile_size = 40

        ##Assets
        self.backgroundAsset = pygame.image.load('Assets\Background\Blue.png')

        self.player = Player(self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
        self.world = World(self.game_data, self.SCREEN_WIDTH, self.SCREEN_HEIGHT, self.tile_size, self.player)
        self.active_sprite_list = pygame.sprite.Group()
        self.background = None

    def draw_text(self, text, size, x, y):
        text_surface = self.font.render(text, True, (255, 0, 0))
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, (300, 300))
        pygame.display.update()

    def initial_Screen(self):
        title = self.font.render("JUMPMAN", True, (255, 0, 0))
        titlePos = title.get_rect(centerx=self.background.get_width() / 2, centery=250)
        self.screen.blit(title, titlePos)

        #initial_screen_image_pos = (self.background.get_width() / 2 - 310, 160)
        #self.screen.blit(initial_screen_image, initial_screen_image_pos)

        description = self.font.render("press any key to start", True, (0,255,0))
        descriptionPos = description.get_rect(centerx=self.background.get_width() / 2, centery=330)
        self.screen.blit(description, descriptionPos)



    def restartGame(self):
        self.game_data = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 1, 1, 1, 2, 2, 1, 1, 1, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        ]
        self.background = pygame.transform.scale(self.backgroundAsset, (self.SCREEN_WIDTH, self.SCREEN_HEIGHT))

        self.active_sprite_list = pygame.sprite.Group()
        self.player = Player(self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
        self.player.rect.x = 500
        self.player.rect.y = self.SCREEN_HEIGHT - self.player.rect.height - self.tile_size

        self.world = World(self.game_data, self.SCREEN_WIDTH, self.SCREEN_HEIGHT, self.tile_size, self.player)

        self.active_sprite_list.add(self.player)
        self.player.level = self.world
        self.player.gameOver = False
        print("Game Over İçi")

    def startGame(self):
        self.restartGame()
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    self.initialScreen = False
            if self.initialScreen:
                self.initial_Screen()
            else:
                if self.player.gameOver:
                    self.draw_text("GAME OVER", 30, 300, 300)
                    pygame.time.wait(1500)
                    self.restartGame()


                self.clock.tick(self.FPS)
                self.screen.blit(self.background, (0, 0))
                self.active_sprite_list.update()
                self.world.update()
                self.world.draw(self.screen)
                self.active_sprite_list.draw(self.screen)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.run = False

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                            self.player.go_lef()
                        if event.key == pygame.K_RIGHT:
                            self.player.go_right()
                        if event.key == pygame.K_SPACE:
                            self.player.jump()
                        if event.key == pygame.K_UP:
                            if pygame.sprite.spritecollide(self.player, self.world.ladder_list, False):
                                self.player.isClimbing = True
                                self.player.climb()
                        if event.key == pygame.K_DOWN:
                            if pygame.sprite.spritecollide(self.player, self.world.ladder_list, False):
                                self.player.isClimbing = True
                                self.player.climb_down()

                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_LEFT and self.player.change_x < 0:
                            self.player.stop()
                        if event.key == pygame.K_RIGHT and self.player.change_x > 0:
                            self.player.stop()
                self.player.rect.clamp_ip(self.screen.get_rect())
            pygame.display.flip()


if __name__ == "__main__":
    pygame.init()
    game = MainLogic()
    game.startGame()
