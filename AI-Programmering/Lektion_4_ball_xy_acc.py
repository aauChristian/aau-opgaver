import pygame
import math

pygame.init()
screen_size = (640, 480)
screen = pygame.display.set_mode(screen_size)
screen.fill((255, 255, 255))

position = [screen_size[0]//2, screen_size[1]//2]
radius = 25
i = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.fill((255, 255, 255))

    current_position = (position [0], position [1] + math.sin(i)*200)
    i += 0.005

    pygame.draw.circle(screen, (0, 0, 0), current_position, radius)
    pygame.display.flip()