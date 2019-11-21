import pygame
import math

def draw_stick_figure(screen, x, y):
    pygame.draw.ellipse(screen, BLACK, [10 + x, -10 + y, 80, 80], 0)
    pygame.draw.line(screen, BLACK, [50 + x, 170 + y], [100 + x, 270 + y], 5)
    pygame.draw.line(screen, BLACK, [50 + x, 170 + y], [x, 270 + y], 5)
    pygame.draw.line(screen, BLACK, [50 + x, 170 + y], [50 + x, 70 + y], 5)
    pygame.draw.line(screen, BLACK, [50 + x, 70 + y], [90 + x, 170 + y], 5)
    pygame.draw.line(screen, BLACK, [50 + x, 70 + y], [10 + x, 170 + y], 5)

pygame.init()

size = (700, 500)
screen = pygame.display.set_mode(size)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (131, 242, 131)
RED = (236, 112, 112)
BLUE = (144, 210, 216)
GREY = (185, 185, 185)
LIGHT_ORANGE = (247, 194, 151)

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
 
    screen.fill(GREY)
    # --- Drawing code should go here

    draw_stick_figure(screen, 300, 150)

    pygame.draw.rect(screen, WHITE, [rect_x, rect_y, 50, 50])
    pygame.draw.rect(screen, LIGHT_ORANGE, [rect_x + 10, rect_y + 10, 30, 30])
    
    rect_x += rect_change_x
    rect_y += rect_change_y

    if rect_x > 650 or rect_x < 0:
        rect_change_x = rect_change_x * -1
    if rect_y > 450 or rect_y < 0:
        rect_change_y = rect_change_y * -1

   
   
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()