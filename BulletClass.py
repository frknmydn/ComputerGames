import random
import pygame
import PlayerClass

class Bullet(pygame.sprite.Sprite):
    def __init__(self, flag, tile_size, SCREEN_WIDTH, SCREEN_HEIGHT, player):
        pygame.sprite.Sprite.__init__(self)
        super().__init__()
        self.flag = flag
        self.player = player
        self.SCREEN_WIDTH = SCREEN_WIDTH
        self.SCREEN_HEIGHT = SCREEN_HEIGHT
        bulletAsset = pygame.image.load('Assets\Player\pinky_idle2.png')
        self.image = pygame.transform.scale(bulletAsset, (round(tile_size / 2), round(tile_size / 2)))
        self.rect = self.image.get_rect()
        self.level = None

        if flag == 1:
            self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width)
            self.rect.y = random.randrange(-50, -40)
            self.speedy = random.randrange(3, 8)

        if flag == 2:
            self.rect.y = random.randrange(SCREEN_HEIGHT - self.rect.height)
            self.rect.x = random.randrange(40, 50)
            self.speedy = random.randrange(1, 8)

        if flag == 3:
            self.rect.y = random.randrange(SCREEN_HEIGHT - self.rect.height)
            self.rect.x = random.randrange(720, 800)
            self.speedy = random.randrange(1, 8)



    def update(self):
        if self.flag == 1:
            self.rect.y += self.speedy
            if self.rect.top > self.SCREEN_HEIGHT + 10:
                maxX = self.player.rect.x + 50
                minX = self.player.rect.x - 50
                if minX < 0:
                    minX += 5
                if maxX > self.SCREEN_WIDTH:
                    maxX -= 5

                self.rect.x = random.randrange(minX, maxX)
                self.rect.y = random.randrange(-50, 40)
                self.speedy = random.randrange(1, 8)

        elif self.flag == 2:
            self.rect.x += self.speedy
            if self.rect.left > self.SCREEN_WIDTH + 10:
                maxY = self.player.rect.y + 50
                minY = self.player.rect.y - 50
                if minY < 0:
                    minY += 5
                if maxY > self.SCREEN_HEIGHT:
                    maxY -= 5

                self.rect.y = random.randrange(minY, maxY)
                self.rect.x = random.randrange(40, 50)
                self.speedy = random.randrange(1, 8)

        elif self.flag == 3:
            self.rect.x -= self.speedy
            if self.rect.right < 0 - self.rect.width:
                maxY = self.player.rect.y + 50
                minY = self.player.rect.y - 50
                if minY < 0:
                    minY += 5
                if maxY > self.SCREEN_HEIGHT:
                    maxY -= 5

                self.rect.y = random.randrange(minY,maxY)
                self.rect.x = random.randrange(720, 800)
                self.speedy = random.randrange(1, 8)