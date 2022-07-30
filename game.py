import pygame
from pygame import mixer
import time
from entities import Paddle, Ball

GAME_WIDTH = 800
GAME_HEIGHT = 600
GAME_TITLE = "PING-PONG"
FPS = 60

pygame.init()
pygame.display.set_caption(GAME_TITLE)
screen = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))

appRunning = True

# Player Initialization
paddle = Paddle(screen, GAME_WIDTH, GAME_HEIGHT)
ball = Ball(screen)

# Delta time implementation for Constant Movement
clock = pygame.time.Clock()
prev_time = time.time()

# Main Loop
while appRunning:
    screen.fill((0, 0, 0))

    # Deltatime
    clock.tick(FPS)
    now = time.time()
    dt = now - prev_time
    prev_time = now

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            appRunning = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and event.key != pygame.K_RIGHT:
                paddle.moveLeft(dt)
            if event.key == pygame.K_RIGHT and event.type != pygame.K_LEFT:
                paddle.moveRight(dt)

        if event.type == pygame.KEYUP:
            paddle.x_offset = 0
    ball.draw()

    paddle.update()
    pygame.display.update()
