import pygame, sys

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Tegn cirkler")
center = (640//2, 480//2)

screen.fill((255, 255, 255))
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.pos[0] > 320 and event.pos[1] < 240:
                pygame.draw.circle(screen, (0, 255, 255), event.pos, 20)
            elif event.pos[0] < 320 and event.pos [1] < 240:
                pygame.draw.circle(screen, (255, 0, 255), event.pos, 20)
            elif event.pos[0] < 320 and event.pos[1] > 240:
                pygame.draw.circle(screen, (255, 255, 0), event.pos, 20)
            else:
                pygame.draw.circle(screen, (0, 0, 0), event.pos, 20)
            
            pygame.display.flip()