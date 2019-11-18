import pygame

pygame.init()

size = (700, 500)
screen = pygame.display.set_mode(size)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
 
    screen.fill(WHITE)
    # --- Drawing code should go here
    for x_offset in range(30, 300, 30):
        pygame.draw.line(screen, GREEN, [x_offset, 100], [x_offset-10, 90], 2)
        pygame.draw.line(screen, RED, [x_offset, 90], [x_offset-10, 100], 2)
        pygame.draw.line(screen, BLUE, [x_offset, 300], [x_offset-10, 290], 2)
        pygame.draw.line(screen, BLACK, [x_offset, 290], [x_offset-10, 300], 2)
   
    pygame.draw.rect(screen, BLUE, [30, 150, 230, 90], 2)
   
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()