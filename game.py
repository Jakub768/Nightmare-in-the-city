import pygame
pygame.init()

WINDOW = pygame.display.set_mode([500,500])
RUNNING = True

while RUNNING:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False 

    #Draw the circle by filling background, define circle colour which have 75 radius
    WINDOW.fill((255,255,255))
    pygame.draw.circle(WINDOW, (0,0,255), (250,250), 75)
    pygame.display.flip()

pygame.quit()