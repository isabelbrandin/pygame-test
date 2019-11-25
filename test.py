import pygame
import math

def draw_stick_figure(screen, x, y):
    pygame.draw.ellipse(screen, BLACK, [5 + x, -5 + y, 40, 40], 0)
    pygame.draw.line(screen, BLACK, [25 + x, 85 + y], [50 + x, 135 + y], 3)
    pygame.draw.line(screen, BLACK, [25 + x, 85 + y], [x, 135 + y], 3)
    pygame.draw.line(screen, BLACK, [25 + x, 85 + y], [25 + x, 35 + y], 3)
    pygame.draw.line(screen, BLACK, [25 + x, 35 + y], [45 + x, 85 + y], 3)
    pygame.draw.line(screen, BLACK, [25 + x, 35 + y], [5 + x, 85 + y], 3)

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

x_speed = 0
y_speed = 0
x_coord = 300
y_coord = 265

# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
       
        # --- Drawing code should go here
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_speed = -3
            if event.key == pygame.K_RIGHT:
                x_speed = 3
            if event.key == pygame.K_UP:
                y_speed = -3
            if event.key == pygame.K_DOWN:
                y_speed = 3
            
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_speed = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_speed = 0
    
    screen.fill(GREY)
    
    x_coord += x_speed
    y_coord += y_speed
    
    draw_stick_figure(screen, x_coord, y_coord)

    pygame.draw.rect(screen, GREEN, [0, 400, 700, 400], 0)

   
   
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()