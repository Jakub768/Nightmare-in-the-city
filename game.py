import pygame
import os
pygame.init()

os.chdir(os.path.dirname(os.path.abspath(__file__))) 
MainClock = pygame.time.Clock()


WIN_COLOR = (255,255,255)
WINDOW_HEIGHT = 1080
WINDOW_WIDTH = 1920
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

class drawbackground(object):
    def __init__(self,x,y,width,height,colour):
        self.x = x 
        self.y = y
        self.width = width
        self.height = height
        self.colour = colour
    
    def drawrect(self,WINDOW):
        pygame.draw.rect(WINDOW, self.colour, pygame.Rect(self.x, self.y, self.width, self.height))

def redrawwindow():
    WINDOW.fill(WIN_COLOR)
    person.draw(WINDOW)
    building.drawrect(WINDOW)

    pygame.display.update()

person = player(200,410,128,128)
building = drawbackground(300,600,100,100,(127,127,127))
RUNNING = True


while RUNNING:
        
    frameMs = MainClock.tick()
    frameSec = frameMs / 1000
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if keys[pygame.K_ESCAPE]:
            RUNNING = False

    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        person.x -= person.vel * frameSec
    elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        person.x += person.vel * frameSec
    elif keys[pygame.K_UP] or keys[pygame.K_w]:
        person.y -= person.vel * frameSec
    elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
        person.y += person.vel * frameSec

    redrawwindow()

pygame.quit()