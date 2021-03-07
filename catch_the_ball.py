import pygame
from pygame.draw import *
from random import randint
import math

pygame.init()

FPS = 40
screen = pygame.display.set_mode((1000, 600))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

pygame.display.update()
clock = pygame.time.Clock()
finished = False

X = randint(170, 980)
X_rect = randint(160, 940)
Y = randint(160, 400)
R = randint(10, 100)
Y_rect = randint(160, 540)
Color = COLORS[randint(0, 5)]
Color_rect = COLORS[randint(0, 5)]
dx = 3
dx_rect = 3
dy = 3
dy_rect = 3
frame_count = 0


def new_ball(color, x, y, r):
    """рисует новый шарик """
    circle(screen, color, (x, y), r)


def new_rect(color, x, y):
    """рисует квадрат"""
    rect(screen, color, (x, y, 50, 50))


while not finished:
    clock.tick(FPS)

    pygame.font.init()
    text_font = pygame.font.Font(None, 60)  # the font to write with
    text_image = text_font.render(str(frame_count), True, (255, 255, 255))
    text_width = text_image.get_width()
    text_height = text_image.get_height()
    text_x = 900  # right-side
    text_y = 0  # top
    screen.blit(text_image, (text_x, text_y))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print('Click!')
            if math.sqrt((event.pos[0] - X) ** 2 + (event.pos[1] - Y) ** 2) <= R:
                frame_count += 1
                Color = COLORS[randint(0, 5)]
            elif event.pos[0] - X_rect <= 50 and event.pos[1] - Y_rect <= 50:
                frame_count += 2
                Color_rect = COLORS[randint(0, 5)]

    new_ball(Color, X, Y, R)
    new_rect(Color_rect, X_rect, Y_rect)
    pygame.display.update()
    screen.fill(BLACK)
    if X + dx >= 1000 - R or X + dx <= R:
        dx = -dx
    if Y + dy >= 600 - R or Y + dy <= R:
        dy = -dy
    if X_rect + dx_rect >= 950 or X_rect + dx_rect <= 0:
        dx_rect = -dx_rect
    if Y_rect + dy_rect >= 550 or Y_rect + dy_rect <= 0:
        dy_rect = -dy_rect
    X += dx
    Y += dy
    X_rect += dx_rect
    Y_rect += dy_rect
pygame.quit()
