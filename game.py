import pygame
import os
pygame.init()
os.chdir(os.path.dirname(os.path.abspath(__file__))) #this will allow me to work on the directory that I am on as without it (for example: everything is on D drive whilst system is on C drive for me), pygame thinks the directory should be in C drive but I don't work on that drive


MainClock = pygame.time.Clock()
WIN_COLOR = (255,255,255)
WINDOW_HEIGHT = 500
WINDOW_WIDTH = 500
WIN_COLOR = (255,255,255)
WINDOW = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
position = [WINDOW_WIDTH/2, WINDOW_HEIGHT/2]

playerImg = pygame.image.load('assets/graphics/PNG/Player/Poses/Player_idle.png')
playerImg.convert()
playerRect = playerImg.get_rect()
playerRect.center = 250, 250

MOVE_SPEED = 100
MoveLeft = False
MoveRight = False
MoveUp = False
MoveDown = False

RUNNING = True

while RUNNING:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                MoveLeft = True
            if event.key == pygame.K_RIGHT:
                MoveRight = True
            if event.key == pygame.K_UP:
                MoveUp = True
            if event.key == pygame.K_DOWN:
                MoveDown = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                MoveLeft = False
            if event.key == pygame.K_RIGHT:
                MoveRight = False
            if event.key == pygame.K_UP:
                MoveUp = False
            if event.key == pygame.K_DOWN:
                MoveDown = False
        
    frameMs = MainClock.tick()
    frameSec = frameMs / 1000

    # move based on bool vars
    #Get amount moved but multiplying speed by time passed (d=vxt)
    if MoveLeft == True:
        position[0] -= MOVE_SPEED * frameSec
    if MoveRight == True:
        position[0] += MOVE_SPEED * frameSec
    if MoveUp == True:
        position[1] -= MOVE_SPEED * frameSec
    if MoveDown == True:
        position[1] += MOVE_SPEED * frameSec



    MoveLeft = False
    MoveRight = False
    MoveUp = False
    MoveDown = False


    WINDOW.fill(WIN_COLOR)
    WINDOW.blit(playerImg)
    pygame.display.flip()


pygame.quit()