import pygame
from pygame import mixer

GAME_WIDTH = 800
GAME_HEIGHT = 600
GAME_TITLE = "H4CK3D"

pygame.init()


class Paddle():
    def __init__(self, screen, width, height):
        # Position
        self.x = 300
        self.y = 550
        self.x_offset = 0
        self.speed = 7

        # Surrounding Environemnt
        self.game_width = width
        self.game_height = height
        self.screen = screen

        # Properties
        self.color = (255, 255, 255)
        self.sizeX = 100
        self.sizeY = 20

    def draw(self):
        pygame.draw.rect(self.screen, self.color,
                         pygame.Rect(self.x, self.y, self.sizeX, self.sizeY))

    def moveRight(self):
        self.x_offset += self.speed

    def moveLeft(self):
        self.x_offset -= self.speed

    def update(self):  # Run this in order to create paddle
        pygame.draw.rect(self.screen, self.color,
                         pygame.Rect(self.x, self.y, self.sizeX, self.sizeY))
        self.x += self.x_offset

        if self.x >= (self.game_width - 64):
            self.x = 736
        if self.x <= 0:
            self.x = 0


class Obstacle():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.speed = 6

    def draw(self):
        pass

    def update():
        pass


appRunning = True
# Player Initialization

screen = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
paddle = Paddle(screen, 800, 600)

pygame.display.set_caption(GAME_TITLE)
clock = pygame.time.Clock()
# Main Loop
while appRunning:
    screen.fill((0, 0, 0))
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            appRunning = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                paddle.moveLeft()
            if event.key == pygame.K_RIGHT and event.type != pygame.K_LEFT:
                paddle.moveRight()

        if event.type == pygame.KEYUP:
            paddle.x_offset = 0

    paddle.update()  # Update Function
    # screen.blit(paddle.image, (paddle.x, paddle.y))
    pygame.display.flip()
