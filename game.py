import pygame
import os
pygame.init()

os.chdir(os.path.dirname(os.path.abspath(__file__))) 
MainClock = pygame.time.Clock()

WIN_COLOR = (255,255,255)
WINDOW_HEIGHT = 1080
WINDOW_WIDTH = 1920
WINDOW = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
RUNNING = True

class Player(object):
    def __init__(self,x,y,width,height):
        self.x = x 
        self.y = y 
        self.width = width
        self.height = height 
        self.vel = 400
    
    def drawPlayer(self, WINDOW):
        playerImg = pygame.image.load('assets/graphics/PNG/Player/Poses/Player_idle.png')
        playerImg.convert()
        WINDOW.blit(playerImg, (self.x,self.y))

class projectile(object):
    def __init__(self, bulletx, bullety, radius, colour, width):
        self.bulletx = bulletx
        self.bullety = bullety
        self.radius = radius
        self.colour = colour
        self.width = width
        self.velocity = 400
        self.numOfBullets = 5

    def drawBullet(self, WINDOW):
        pygame.draw.circle(WINDOW, self.colour, (self.bulletx, self.bullety), self.radius, self.width)
    

class DrawBackground(object):
    def __init__(self,x,y,width,height,colour):
        self.x = x 
        self.y = y
        self.width = width
        self.height = height
        self.colour = colour

    def drawRectangle(self,WINDOW):
        pygame.draw.rect(WINDOW, self.colour, pygame.Rect(self.x, self.y, self.width, self.height))

def prepareGame():
    WINDOW.fill(WIN_COLOR)
    drawMainStreet()
    drawMiscellaneous()
    drawBullet()

def drawMainStreet():
    building = DrawBackground(0,400,200,700,(127,127,127))
    oppositeBuilding = DrawBackground(1720,400,200,700,(127,127,127))
    topBuilding = DrawBackground(0,0,1920,100,(127,127,127))

    building.drawRectangle(WINDOW)
    oppositeBuilding.drawRectangle(WINDOW)
    topBuilding.drawRectangle(WINDOW)


def drawMiscellaneous():
    person.drawPlayer(WINDOW)

def drawBullet():
    for bullet in BulletList:
        bullet.drawBullet(WINDOW)
        bullet.bullety -= bullet.velocity * frameSec

#Define characters and other properties in the game
person = Player(912,WINDOW_WIDTH/2,128,128)
BulletList = []

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

    if keys[pygame.K_SPACE]:
        BulletList.append(projectile(person.x+person.width//3,person.y+person.height//2,7,(255,255,0),6))

    pygame.display.update()
    prepareGame()

pygame.quit()