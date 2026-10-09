import pygame
import math

pygame.init()
screen_size = (640, 480)
screen = pygame.display.set_mode(screen_size)
screen.fill((245, 128, 0))

center_point = (screen_size[0]/2, screen_size[1]/2)
start_marking = 180
end_marking = 200
hour_mark_angle_offset = 360/12

# Draw 12 hour markings
for hour_mark_index in range(12):
    angle = hour_mark_angle_offset*hour_mark_index
    start_point = (center_point[0] + math.cos(math.radians(angle))*start_marking,
                   center_point[1] + math.sin(math.radians(angle))*start_marking)
    end_point = (center_point[0] + math.cos(math.radians(angle))*end_marking,
                 center_point[1] + math.sin(math.radians(angle))*end_marking)
    pygame.draw.line(screen, (0, 0, 0), start_point, end_point, 5)

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


