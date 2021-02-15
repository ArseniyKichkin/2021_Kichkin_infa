import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))
gray = (128, 128, 128)
screen.fill(gray)


circle(screen, (255, 255, 0), (200, 200), 100)
rect(screen, (0,0,0), (145, 245, 110, 25), 0)
circle(screen, (255,0,0), (150, 165), 20)
circle(screen, (255,0,0), (250,165), 16)
circle(screen, (0,0,0), (150, 165), 10)
circle(screen, (0,0,0), (250,165), 6)
polygon(screen, (0,0,0), ((104, 110), (188, 155), (185, 160), (101, 114)), 0)
polygon(screen, (0,0,0), ((210, 155), (299, 116), (301, 119), (212, 160)))


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()