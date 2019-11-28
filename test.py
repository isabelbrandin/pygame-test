import pygame
import math

def draw_stick_figure(screen, x, y):
    pygame.draw.ellipse(screen, BLACK, [1 + x, y, 10, 10], 0)
    pygame.draw.line(screen, BLACK, [5 + x, 17 + y], [10 + x, 27 + y], 2)
    pygame.draw.line(screen, BLACK, [5 + x, 17 + y], [x, 27 + y], 2)
    pygame.draw.line(screen, BLUE, [5 + x, 17 + y], [5 + x, 7 + y], 2)
    pygame.draw.line(screen, BLUE, [5 + x, 7 + y], [9 + x, 17 + y], 2)
    pygame.draw.line(screen, BLUE, [5 + x, 7 + y], [1 + x, 17 + y], 2)

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
 
clock = pygame.time.Clock()

x_speed = 0
y_speed = 0
x_coord = 300
y_coord = 265

# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True 
       
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

    screen.fill(WHITE)
    
    x_coord += x_speed
    y_coord += y_speed

    if x_coord > 686 or x_coord < 5:
        x_speed = 0
    if y_coord > 470 or y_coord < 7:
        y_speed = 0
    
    draw_stick_figure(screen, x_coord, y_coord)
   
   
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()