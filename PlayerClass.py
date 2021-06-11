import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        playerAsset = pygame.image.load('Assets\Player\pinky_idle1.png')
        super().__init__()

        self.width = 25
        self.height = 25
        self.SCREEN_WIDTH = SCREEN_WIDTH
        self.SCREEN_HEIGHT = SCREEN_HEIGHT
        self.image = pygame.transform.scale(playerAsset, (self.width, self.height))
        self.rect = self.image.get_rect()
        self.change_x = 0
        self.change_y = 0
        self.isClimbing = False
        self.gameOver = False
        self.level = None
        self.levelComplete = False
        self.currentLevel = 1
        self.walkCount = 0
        self.jump_sound = pygame.mixer.Sound("Sounds\jump.wav")
        self.coin_sound = pygame.mixer.Sound("Sounds\gold.wav")
        self.dead_sound = pygame.mixer.Sound("Sounds\gameover.wav")
        self.standCount = 0
        self.walkLeft = False
        self.walkRight = False
        self.walkLeftSprite = [
            pygame.image.load("Assets\Player\pinky_runLeft1.png"), pygame.image.load("Assets\Player\pinky_runLeft2.png"),
            pygame.image.load("Assets\Player\pinky_runLeft3.png")
        ]

        self.walkRightSprite = [
            pygame.image.load("Assets\Player\pinky_runRight1.png"), pygame.image.load("Assets\Player\pinky_runRight2.png"),
            pygame.image.load("Assets\Player\pinky_runRight3.png")
        ]

        self.IdleSprite = [
            pygame.image.load("Assets\Player\pinky_idle1.png"),
            pygame.image.load("Assets\Player\pinky_idle2.png"),
            pygame.image.load("Assets\Player\pinky_idle3.png"),
            pygame.image.load("Assets\Player\pinky_idle4.png")
        ]

    def update(self, screen):



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
                self.coin_sound.play()
                self.level.coinAmount += 1
                if self.level.coinAmount >= 5:
                    self.levelComplete = True
                    self.currentLevel += 1

                    print(self.currentLevel)


        bullet_hit_list = pygame.sprite.spritecollide(self, self.level.enemy_list, False)
        if bullet_hit_list:
            self.dead_sound.play()
            print("Game Over")
            self.gameOver = True

        if self.walkCount + 1 >= 9:
            self.walkCount = 0
        elif self.standCount + 1 >= 24:
            self.standCount = 0

        if self.walkLeft:
            self.image = pygame.transform.scale(self.walkLeftSprite[self.walkCount // 3], (self.width, self.height))
            #self.image = self.walkLeftSprite[self.walkCount // 3]
            #screen.blit(self.walkLeftSprite[self.walkCount // 3],
             #           (self.change_x, self.change_y))
            self.walkCount += 1
            self.standCount = 0

        elif self.walkRight:
            self.image = pygame.transform.scale(self.walkRightSprite[self.walkCount // 3], (self.width, self.height))
            #self.image = self.walkRightSprite[self.walkCount // 3]
            #screen.blit(self.walkRightSprite[self.walkCount // 3],
             #           (self.change_x, self.change_y))
            self.walkCount += 1
            self.standCount = 0

        else:
            self.image = pygame.transform.scale(self.IdleSprite[self.standCount // 6], (self.width, self.height))
            self.standCount += 1
            self.walkCount = 0




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
        self.jump_sound.play()
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