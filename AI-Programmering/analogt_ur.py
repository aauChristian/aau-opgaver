import pygame
import math
import time

pygame.init()
screen = pygame.display.set_mode((640, 480))
screen.fill((120, 255, 255))

# Sekund-, minut- og timeviserens længder
start_point = (320, 240)
s_length = 170 
m_length = 135 
h_length = 80 

while True:
    # Tegner sekundviseren
    screen.fill((120, 255, 255))
    current_time = time.localtime()
    seconds = current_time.tm_sec
    angle = seconds * 6 + 270   # 1 sekund er 6 grader. Offset på 270 grader for at starte i toppen.
    end_x = start_point[0] + s_length * math.cos(math.radians(angle))
    end_y = start_point[1] + s_length * math.sin(math.radians(angle))
    end_point = (end_x, end_y)
    pygame.draw.line(screen, (255,0,0), start_point, end_point, 3)

    # Tegner minutviseren
    minutes = current_time.tm_min
    angle = minutes * 6 + 270   # 1 minut er 6 grader. Offset på 270 grader for at starte i toppen.
    end_x = start_point[0] + m_length * math.cos(math.radians(angle))
    end_y = start_point[1] + m_length * math.sin(math.radians(angle))
    end_point = (end_x, end_y)
    pygame.draw.line(screen, (255,0,255), start_point, end_point, 3)

    # Tegner timeviseren
    hours = current_time.tm_hour
    angle = hours * 30 + 270   # 1 time er 30 grader. Offset på 270 grader for at starte i toppen.
    end_x = start_point[0] + h_length * math.cos(math.radians(angle))
    end_y = start_point[1] + h_length * math.sin(math.radians(angle))
    end_point = (end_x, end_y)
    pygame.draw.line(screen, (0,0,255), start_point, end_point, 3)

    # Tegner 12 time markeringer
    start_point = (320, 240)
    radius = 200

    for hour_marks in range(12):
        angle = hour_marks * 30 + 270
        outer_x = start_point[0] + radius * math.cos(math.radians(angle))
        outer_y = start_point[1] + radius * math.sin(math.radians(angle))

        inner_x = start_point[0] + (radius-20) * math.cos(math.radians(angle))
        inner_y = start_point[1] + (radius-20) * math.sin(math.radians(angle))

        pygame.draw.line(screen, (0, 0, 0), (outer_x, outer_y), (inner_x, inner_y), 3)

    # Tegner tallene 1-12 ud fra time markeringerne
    numbers = [12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    font = pygame.font.Font(None, 30)

    for i in range(12):
        number = numbers [i]
        angle = i * 30 + 270

        text_x = start_point[0] + (radius - 35) * math.cos(math.radians(angle))
        text_y = start_point[1] + (radius - 35) * math.sin(math.radians(angle))

        text = font.render(str(number), True, (0, 0, 0))
        text_rect = text.get_rect(center=(text_x, text_y))
        screen.blit(text, text_rect)

    # Tegner Urskiven
    pygame.draw.circle(screen, (0, 0, 0), start_point, 200, 3)
    pygame.draw.circle(screen, (255, 255, 255), start_point, 205, 3)
                                                            
    time.sleep(1)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()