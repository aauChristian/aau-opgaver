import pygame
import math
from datetime import datetime

pygame.init()
screen = pygame.display.set_mode((640, 480))
screen.fill((255, 255, 255))

start_point = [640//2, 480//2]
radius = 25
direction = 1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.fill((255, 255, 255))

    pygame.draw.circle(screen, (0, 0, 0), start_point, radius)
    start_point[1] += 0.5*direction

    if start_point[1] > 480-radius or start_point[1] < 0+radius:
        direction *= -1

    pygame.display.flip()