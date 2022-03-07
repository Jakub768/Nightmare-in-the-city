import pygame
pygame.init()

WINDOW = pygame.display.set_mode([500,500])
RUNNING = True


playerImg = pygame.image.load('assets/graphics/PNG/Player/Poses/Player_idle.png')
playerImg.convert()
playerRect = playerImg.get_rect()
playerRect.center = 250, 250


while RUNNING:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False 

    #Draw everything
    WINDOW.fill((255,255,255))
    pygame.draw.circle(WINDOW, (0,0,255), (375,375), 75)
    WINDOW.blit(playerImg, playerRect)
    pygame.display.flip()

pygame.quit()