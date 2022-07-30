import pygame as pg


class Paddle():
    def __init__(self, screen, width, height):
        # Position
        self.x = 300
        self.y = 550
        self.x_offset = 0
        self.speed = 500

        # Surrounding Environemnt
        self.game_width = width
        self.game_height = height
        self.screen = screen

        # Properties
        self.color = (255, 255, 255)
        self.sizeX = 120
        self.sizeY = 20

    def moveRight(self, dt):
        self.x_offset += self.speed * dt

    def moveLeft(self, dt):
        self.x_offset -= self.speed * dt

    def update(self):
        pg.draw.rect(self.screen, self.color,
                     pg.Rect(self.x, self.y, self.sizeX, self.sizeY))
        self.x += self.x_offset

        # Applying Offset by rectangluar shape
        if self.x >= (self.game_width - self.sizeX):
            self.x = self.game_width - self.sizeX
        if self.x <= 0:
            self.x = 0


class Ball():
    def __init__(self, screen):
        self.x = 50
        self.y = 550
        self.angle = 45
        self.screen = screen

        self.color = (255, 255, 255)

    def draw(self):
        pg.draw.circle(self.screen, self.color, (self.x, self.y), 10)

    def move(self):
        pass

    def update(self):
        pg.draw.circle(self.screen, self.color, (self.x, self.y), 100)
