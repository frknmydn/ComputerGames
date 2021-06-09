import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        playerAsset = pygame.image.load('Assets\Player\pinky_runRight1.png')
        super().__init__()

        width = 25
        height = 25
        self.SCREEN_WIDTH = SCREEN_WIDTH
        self.SCREEN_HEIGHT = SCREEN_HEIGHT
        self.image = pygame.transform.scale(playerAsset, (width, height))
        self.rect = self.image.get_rect()
        self.change_x = 0
        self.change_y = 0
        self.isClimbing = False
        self.gameOver = False
        self.level = None
        self.levelComplete = False
        self.currentLevel = 1

    def update(self):
        self.calculate_gravity()
        self.rect.x += self.change_x
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                self.rect.left = block.rect.right

        self.rect.y += self.change_y
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            if not self.isClimbing:
                if self.change_y > 0:
                    self.rect.bottom = block.rect.top
                elif self.change_y < 0:
                    self.rect.top = block.rect.bottom

            self.change_y = 0

        block_hit_list = pygame.sprite.spritecollide(self, self.level.ladder_list, False)
        if not block_hit_list:
            self.isClimbing = False
        else:
            if self.isClimbing:
                for block in block_hit_list:
                    """""
                    if len(block_hit_list) > 0:
                    """""
        coin_hit_list = pygame.sprite.spritecollide(self, self.level.coin_list, True)
        for coin in coin_hit_list:
            if self.rect.colliderect(coin.rect):
                self.level.coinAmount += 1
                if self.level.coinAmount >= 5:
                    self.levelComplete = True
                    self.currentLevel += 1
                    print(self.currentLevel)


        bullet_hit_list = pygame.sprite.spritecollide(self, self.level.enemy_list, False)
        if bullet_hit_list:
            print("Game Over")
            self.gameOver = True




    def calculate_gravity(self):

        if not self.isClimbing:
            if self.change_y == 0:
                self.change_y = 1
            else:
                self.change_y += .25

            if self.rect.y >= self.SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
                self.change_y = 0
                self.rect.y = self.SCREEN_HEIGHT - self.rect.height

    def jump(self):

        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 2

        if len(platform_hit_list) > 0:
            self.change_y = -5

    def climb(self):
        self.change_y = -1.5

    def climb_down(self):
        self.change_y = +2

    def go_lef(self):
        self.change_x = -6

    def go_right(self):
        self.change_x = +6

    def stop(self):
        self.change_x = 0