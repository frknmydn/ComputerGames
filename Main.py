import pygame
from pygame.locals import *

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Oyun')

# variables
tile_size = 40

##Assets
backgroundAsset = pygame.image.load('Assets\Background\Blue.png')


def draw_grid():
    for line in range(0, round(SCREEN_WIDTH / tile_size)):
        pygame.draw.line(screen, (255, 255, 255), (line * tile_size, 0), (line * tile_size, SCREEN_HEIGHT))
        for line in range(0, round(SCREEN_HEIGHT / tile_size)):
            pygame.draw.line(screen, (255, 255, 255), (0, line * tile_size), (SCREEN_WIDTH, line * tile_size))


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        width = 25
        height = 25
        self.image = pygame.Surface([width, height])
        self.rect = self.image.get_rect()
        self.change_x = 0
        self.change_y = 0
        self.isClimbing = False

        self.level = None

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
                    print(len(block_hit_list))

    def calculate_gravity(self):

        if not self.isClimbing:
            if self.change_y == 0:
                self.change_y = 1
            else:
                self.change_y += .25

            if self.rect.y >= SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
                self.change_y = 0
                self.rect.y = SCREEN_HEIGHT - self.rect.height

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


class Brick(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        stoneAsset = pygame.image.load('Assets\Terrain\Stone.png')
        super().__init__()

        self.image = pygame.transform.scale(stoneAsset, (tile_size, tile_size))
        self.rect = self.image.get_rect()
        self.rect.x = x * tile_size
        self.rect.y = y * tile_size


class Ladder(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        super().__init__()
        self.image = pygame.Surface((tile_size, tile_size))
        self.image.fill(pygame.Color("blue"))
        self.rect = self.image.get_rect()
        self.rect.x = x * tile_size
        self.rect.y = y * tile_size


class Level(object):
    def __init__(self, player):
        self.ladder_list = pygame.sprite.Group()
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.player = player

    def update(self):
        self.ladder_list.update(())
        self.platform_list.update()
        self.enemy_list.update()

    def draw(self, screen):
        self.ladder_list.draw(screen)
        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)


class World(Level):
    def __init__(self, data):

        Level.__init__(self, player)

        self.tile_list = []
        count_row = 0
        for row in data:
            count_col = 0
            for tile in row:
                if tile == 1:
                    stone = Brick(count_col, count_row)
                    self.tile_list.append(stone)
                    self.platform_list.add(stone)
                elif tile == 2:
                    ladder = Ladder(count_col, count_row)
                    self.tile_list.append(ladder)
                    self.ladder_list.add(ladder)

                count_col += 1
            count_row += 1

    def draw(self, screen):
        self.platform_list.draw(screen)
        self.ladder_list.draw(screen)
        # for tile in self.tile_list:
        #   screen.blit(tile)


game_data = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 1, 1, 1, 2, 2, 1, 1, 1, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

active_sprite_list = pygame.sprite.Group()
player = Player()
player.rect.x = 500
player.rect.y = SCREEN_HEIGHT - player.rect.height - tile_size
world = World(game_data)
active_sprite_list.add(player)
run = True
player.level = world

while run:
    background = pygame.transform.scale(backgroundAsset, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(background, (0, 0))
    draw_grid()
    active_sprite_list.update()
    world.draw(screen)
    active_sprite_list.draw(screen)
    print(player.isClimbing)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.go_lef()
            if event.key == pygame.K_RIGHT:
                player.go_right()
            if event.key == pygame.K_SPACE:
                player.jump()
            if event.key == pygame.K_UP:
                if pygame.sprite.spritecollide(player, world.ladder_list, False):
                    player.isClimbing = True
                    player.climb()
            if event.key == pygame.K_DOWN:
                if pygame.sprite.spritecollide(player, world.ladder_list, False):
                    player.isClimbing = True
                    player.climb_down()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT and player.change_x < 0:
                player.stop()
            if event.key == pygame.K_RIGHT and player.change_x > 0:
                player.stop()
    player.rect.clamp_ip(screen.get_rect())
    pygame.display.flip()

pygame.quit()