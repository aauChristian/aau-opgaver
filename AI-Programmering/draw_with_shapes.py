import pygame

pygame.init() # Initialize Pygame
screen = pygame.display.set_mode((640, 480)) # Create a window of 640x480 pixels
screen.fill((255, 255, 255)) # Fill the screen with white

pygame.draw.line(screen, (38, 255, 38), (0, 380), (640, 380), 5) # Draw ground
pygame.draw.polygon(screen, (38,255,38), [(0, 380), (640, 380), (640, 480), (0, 480)]) # Fill the ground with green color
pygame.draw.line(screen, (255, 45, 45), (200,380), (200,250), 5)# Draw the left wall
pygame.draw.line(screen, (255, 45, 45), (440,380), (440,250), 5)# Draw the right wall
pygame.draw.line(screen, (200, 45, 45), (200,250), (440,250), 5)# Draw the roof
pygame.draw.line(screen, (255, 45, 45), (200,250), (320, 150), 5)# Draw the left diagonal roof
pygame.draw.line(screen, (255, 45, 45), (440,250), (320,150), 5)# Draw the right diagonal roof
pygame.draw.rect(screen, (255, 45, 45), (200, 250, 240, 130)) # fill the house with red color
pygame.draw.polygon(screen, (255, 45, 45), [(200, 250), (440, 250), (320, 150)]) # Fill the triangle in the roof with red color
pygame.draw.rect(screen, (145, 255, 255), (220, 320, 20, 20)) # Draw the left window
pygame.draw.rect(screen, (145, 255, 255), (400, 320, 20, 20)) # Draw the right window
pygame.draw.circle(screen, (145, 255, 255), (320, 200), 20) # Draw the window on the roof   
pygame.draw.rect(screen, (138, 60, 26), (270, 300, 60, 80)) # Draw the door

# Make sure the window stays open until the user closes it
run_flag = True
while run_flag is True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_flag = False
    pygame.display.flip() # Refresh the screen so drawing appears