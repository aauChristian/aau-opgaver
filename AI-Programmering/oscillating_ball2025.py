import pygame
import math

pygame.init()
screen_size = (640, 480)
screen = pygame.display.set_mode(screen_size)
screen.fill((255, 255, 255))

position = [screen_size[0]//2, screen_size[1]//2]
radius = 25
direction = 1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.fill((255, 255, 255))

    pygame.draw.circle(screen, (0, 0, 0), position, radius)
    position[1] += 0.1*direction

    if position[1] > screen_size[1]-radius or position[1] < 0+radius:
        direction *= -1


    pygame.display.flip()
