import pygame
import random

from pygame.locals import *

from LadderClass import Ladder
from PlayerClass import Player
from WorldClass import World
from MapsClass import Map


class MainLogic:
    def __init__(self):

        self.fontName = pygame.font.match_font('comicsansms')
        self.game_data = []
        self.SCREEN_WIDTH = 800
        self.SCREEN_HEIGHT = 800
        self.clock = pygame.time.Clock()
        self.FPS = 60
        self.run = True
        self.background_sound = pygame.mixer.Sound("Sounds\Background.wav")
        self.font = pygame.font.Font(self.fontName, 20)
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.initialScreen = True
        pygame.display.set_caption('Oyun')
        self.mapClass = Map()
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
        self.screen.blit(text_surface, (x, y))



    def initial_Screen(self):
        self.screen.fill((0, 0, 0))
        title = self.font.render("JUMPMAN", True, (255, 0, 0))
        titlePos = title.get_rect(centerx=self.background.get_width() / 2, centery=250)
        self.screen.blit(title, titlePos)

        # initial_screen_image_pos = (self.background.get_width() / 2 - 310, 160)
        # self.screen.blit(initial_screen_image, initial_screen_image_pos)

        description = self.font.render("press any key to start", True, (0, 255, 0))
        descriptionPos = description.get_rect(centerx=self.background.get_width() / 2, centery=330)
        self.screen.blit(description, descriptionPos)

    def restartGame(self, currentLevel):
        self.game_data = self.mapClass.getMap(currentLevel)

        self.background = pygame.transform.scale(self.backgroundAsset, (self.SCREEN_WIDTH, self.SCREEN_HEIGHT))

        self.active_sprite_list = pygame.sprite.Group()
        self.player = Player(self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
        self.player.rect.x = 500
        self.player.rect.y = self.SCREEN_HEIGHT - self.player.rect.height - self.tile_size

        self.world = World(self.game_data, self.SCREEN_WIDTH, self.SCREEN_HEIGHT, self.tile_size, self.player)

        self.active_sprite_list.add(self.player)
        self.player.level = self.world
        self.player.currentLevel = currentLevel
        self.player.gameOver = False
        self.player.level.coinAmount = 0
        print("Game Over İçi")

    def startGame(self):
        self.background_sound.play()
        self.restartGame(self.player.currentLevel)
        if not self.run:
            pygame.quit()
        while self.run:
            if self.initialScreen:
                self.initial_Screen()
                for menuEvent in pygame.event.get():
                    if menuEvent.type == pygame.KEYDOWN:
                        self.initialScreen = False
                    elif menuEvent.type == pygame.QUIT:
                        self.run = False
                pygame.display.flip()

            else:

                if self.player.gameOver:
                    self.draw_text("GAME OVER", 30, 300, 300)
                    pygame.display.update()
                    pygame.time.wait(1500)
                    self.restartGame(1)

                if self.player.levelComplete:
                    if self.player.currentLevel <= 3:
                        self.draw_text("Level Complete", 30, 300, 300)
                        pygame.display.update()
                        pygame.time.wait(1500)
                        self.restartGame(self.player.currentLevel)
                    else:
                        self.player.levelComplete = False
                        self.initialScreen = True
                        self.player.currentLevel = 1
                        self.restartGame(self.player.currentLevel)
                        self.initial_Screen()

                self.clock.tick(self.FPS)
                self.screen.blit(self.background, (0, 0))
                self.active_sprite_list.update(self.screen)
                self.world.update()
                self.world.draw(self.screen)
                self.active_sprite_list.draw(self.screen)

                for playerEvent in pygame.event.get():
                    if playerEvent.type == pygame.QUIT:
                        self.run = False

                    if playerEvent.type == pygame.KEYDOWN:
                        if playerEvent.key == pygame.K_LEFT:
                            self.player.go_lef()
                            self.player.walkLeft = True
                            self.player.walkRight = False

                        elif playerEvent.key == pygame.K_RIGHT:
                            self.player.go_right()
                            self.player.walkRight = True
                            self.player.walkLeft = False

                        if playerEvent.key == pygame.K_SPACE:
                            self.player.jump()
                        if playerEvent.key == pygame.K_UP:
                            if pygame.sprite.spritecollide(self.player, self.world.ladder_list, False):
                                self.player.isClimbing = True
                                self.player.climb()
                        if playerEvent.key == pygame.K_DOWN:
                            if pygame.sprite.spritecollide(self.player, self.world.ladder_list, False):
                                self.player.isClimbing = True
                                self.player.climb_down()

                    if playerEvent.type == pygame.KEYUP:
                        if playerEvent.key == pygame.K_LEFT and self.player.change_x < 0:
                            self.player.stop()
                            self.player.walkRight = False
                            self.player.walkLeft = False
                            self.player.isClimbing = False
                            self.player.walkCount = 0
                        elif playerEvent.key == pygame.K_RIGHT and self.player.change_x > 0:
                            self.player.stop()
                            self.player.walkRight = False
                            self.player.walkLeft = False
                            self.player.isClimbing = False
                            self.player.walkCount = 0

                self.draw_text("Level: {}/3".format(self.player.currentLevel), 10, 10, 10)
                self.draw_text("Coins: {}/5".format(self.player.level.coinAmount), 10, self.screen.get_width() - 100, 10)
                self.player.rect.clamp_ip(self.screen.get_rect())

                pygame.display.flip()


if __name__ == "__main__":
    pygame.init()
    game = MainLogic()
    game.startGame()
