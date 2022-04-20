import pygame
import os
pygame.init()
os.chdir(os.path.dirname(os.path.abspath(__file__))) 
# this will allow me to work on the directory that I am on as without it 
# (for example: everything is on D drive whilst system is on C drive for me), 
# pygame thinks the directory should be in C drive but I don't work on that drive

MainClock = pygame.time.Clock()
WIN_COLOR = (255,255,255)
WINDOW_HEIGHT = 768
WINDOW_WIDTH = 1024
WINDOW = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))


playerImg = pygame.image.load('assets/graphics/PNG/Player/Poses/Player_idle.png')
playerImg.convert()

class player(object):
    def __init__(self,x,y,width,height):
        self.x = x 
        self.y = y 
        self.width = width
        self.height = height 
        self.vel = 500
    
    def draw(self, WINDOW):
        WINDOW.blit(playerImg, (self.x,self.y))

def redrawwindow():
    WINDOW.fill(WIN_COLOR)
    person.draw(WINDOW)

    pygame.display.update()
    

person = player(200,410,128,128)
RUNNING = True
while RUNNING:
        
    frameMs = MainClock.tick()
    frameSec = frameMs / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        person.x -= person.vel * frameSec
    elif keys[pygame.K_RIGHT]:
        person.x += person.vel * frameSec

    redrawwindow()

pygame.quit()