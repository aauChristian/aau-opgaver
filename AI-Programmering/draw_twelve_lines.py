import pygame
import math

pygame.init()
screen = pygame.display.set_mode((640, 480))
screen.fill((255, 255, 255))

start_point = (320, 240)
angle = 0
length = 200
end_x = start_point[0] + length * math.cos(math.radians(angle))
end_y = start_point[1] + length * math.sin(math.radians(angle))
end_point = (end_x, end_y)
pygame.draw.line(screen, (0,0,0), start_point, end_point, 5)

angle = 30
end_x = start_point[0] + length * math.cos(math.radians(angle))
end_y = start_point[1] + length * math.sin(math.radians(angle))
end_point = (end_x, end_y)
pygame.draw.line(screen, (0,0,0), start_point, end_point, 5)

angle = 60
end_x = start_point[0] + length * math.cos(math.radians(angle))
end_y = start_point[1] + length * math.sin(math.radians(angle))
end_point = (end_x, end_y)
pygame.draw.line(screen, (0,0,0), start_point, end_point, 5)

angle = 90
end_x = start_point[0] + length * math.cos(math.radians(angle))
end_y = start_point[1] + length * math.sin(math.radians(angle))
end_point = (end_x, end_y)
pygame.draw.line(screen, (0,0,0), start_point, end_point, 5)

angle = 120
end_x = start_point[0] + length * math.cos(math.radians(angle))
end_y = start_point[1] + length * math.sin(math.radians(angle))
end_point = (end_x, end_y)
pygame.draw.line(screen, (0,0,0), start_point, end_point, 5)

angle = 150
end_x = start_point[0] + length * math.cos(math.radians(angle))
end_y = start_point[1] + length * math.sin(math.radians(angle))
end_point = (end_x, end_y)
pygame.draw.line(screen, (0,0,0), start_point, end_point, 5)

angle = 180
end_x = start_point[0] + length * math.cos(math.radians(angle))
end_y = start_point[1] + length * math.sin(math.radians(angle))
end_point = (end_x, end_y)
pygame.draw.line(screen, (0,0,0), start_point, end_point, 5)

angle = 210
end_x = start_point[0] + length * math.cos(math.radians(angle))
end_y = start_point[1] + length * math.sin(math.radians(angle))
end_point = (end_x, end_y)
pygame.draw.line(screen, (0,0,0), start_point, end_point, 5)

angle = 240
end_x = start_point[0] + length * math.cos(math.radians(angle))
end_y = start_point[1] + length * math.sin(math.radians(angle))
end_point = (end_x, end_y)
pygame.draw.line(screen, (0,0,0), start_point, end_point, 5)

angle = 270
end_x = start_point[0] + length * math.cos(math.radians(angle))
end_y = start_point[1] + length * math.sin(math.radians(angle))
end_point = (end_x, end_y)
pygame.draw.line(screen, (0,0,0), start_point, end_point, 5)

angle = 300
end_x = start_point[0] + length * math.cos(math.radians(angle))
end_y = start_point[1] + length * math.sin(math.radians(angle))
end_point = (end_x, end_y)
pygame.draw.line(screen, (0,0,0), start_point, end_point, 5)

angle = 330
end_x = start_point[0] + length * math.cos(math.radians(angle))
end_y = start_point[1] + length * math.sin(math.radians(angle))
end_point = (end_x, end_y)
pygame.draw.line(screen, (0,0,0), start_point, end_point, 5)

pygame.display.flip()
while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()