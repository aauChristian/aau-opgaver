import pygame, sys

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Tegn polyline")

screen.fill((255, 255, 255))
pygame.display.flip()

punkter = []

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            punkter.append(event.pos)
            if len(punkter) >= 2:
                pygame.draw.lines(screen, (0, 0, 0), False, punkter, 3)

        pygame.display.flip()