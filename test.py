import pygame
import math

pygame.init()

size = (700, 500)
screen = pygame.display.set_mode(size)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (185, 185, 185)
LIGHT_PINK = (247, 194, 151)

done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

rect_x = 50
rect_y = 50
rect_change_x = 5
rect_change_y = 5

# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
 
    screen.fill(BLACK)
    # --- Drawing code should go here

    pygame.draw.rect(screen, WHITE, [rect_x, rect_y, 50, 50])
    pygame.draw.rect(screen, LIGHT_PINK, [rect_x + 10, rect_y + 10, 30, 30])
    
    rect_x += rect_change_x
    rect_y += rect_change_y

    if rect_x > 650 or rect_x < 0:
        rect_change_x = rect_change_x * -1
    if rect_y > 450 or rect_y < 0:
        rect_change_y = rect_change_y * -1

    for x_offset in range(30, 300, 30):
        pygame.draw.line(screen, GREEN, [x_offset, 100], [x_offset-10, 90], 2)
        pygame.draw.line(screen, RED, [x_offset, 90], [x_offset-10, 100], 2)
        pygame.draw.line(screen, BLUE, [x_offset, 300], [x_offset-10, 290], 2)
        pygame.draw.line(screen, GREY, [x_offset, 290], [x_offset-10, 300], 2)
   
   
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()