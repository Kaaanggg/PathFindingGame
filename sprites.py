import pygame as pg
from settings import *
from enum import Enum


class Entity(Enum):
    PLAYER = YELLOW
    ENEMY = RED


class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y, Entitytype=Entity.PLAYER):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(Entitytype.value)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y

    def move(self, dx=0, dy=0, next=None):
        if not self.collide_with_walls(dx, dy):
            self.x += dx
            self.y += dy

        x = self.x + dx
        y = self.y + dy
        if x >= int(GRIDWIDTH) or x < 0:
            return
        if y >= int(GRIDHEIGHT) or y < 0:
            return
        # if BOARD[x][y] == 1:
        #     return
        # self.x += dx
        # self.y += dy
        next()

    def collide_with_walls(self, dx=0,dy=0):
        for wall in self.game.walls:
            if wall.x == self.x + dx and wall.y == self.y + dy:
                return True
        return False
    

    def fixMove(self, dx=0, dy=0):
        self.x = dx
        self.y = dy

    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE

    def position(self, x: bool = False, y: bool = False):
        if (x):
            return self.x
        if (y):
            return self.y
        return (self.x, self.y)


class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        BOARD[x][y] = 1
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
