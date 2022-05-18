import pygame, pygame.freetype
import os
pygame.init()
pygame.mixer.init()

#system based and windows based variable initialisations
os.chdir(os.path.dirname(os.path.abspath(__file__))) 
MainClock = pygame.time.Clock()

WIN_COLOR = (255,255,255)
WINDOW_HEIGHT = 1080
WINDOW_WIDTH = 1920
WINDOW = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
RUNNING = True
GRAY = (127,127,127)

#Classes to define main content such as characters or the map

class Player(object):
    def __init__(self,x,y,width,height):
        self.x = x 
        self.y = y 
        self.width = width
        self.height = height 
        self.vel = 400
        self.playerImg = pygame.image.load('assets/graphics/PNG/Player/Poses/Player_idle.png')
    
    def drawPlayer(self, WINDOW):
        self.playerImg.convert()
        WINDOW.blit(self.playerImg, (self.x,self.y))
    
class Enemy(object):
    def __init__(self,x,y,width,height):
        self.x = x 
        self.y = y
        self.width = width
        self.height = height
        self.enemyImg = pygame.image.load('assets/graphics/PNG/Enemy/zombie_idle.png')

    def drawEnemy(self, WINDOW):
        self.enemyImg.convert()
        WINDOW.blit(self.enemyImg, (self.x,self.y))


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
        self.yellow = pygame.draw.circle(WINDOW, self.colour, (self.bulletx, self.bullety), self.radius, self.width)
    
    def shootBullet(self):
        self.bullety -= self.velocity * frameSec
    

class DrawBackground(object):
    def __init__(self,x,y,width,height,colour):
        self.x = x 
        self.y = y
        self.width = width
        self.height = height
        self.colour = colour

    def drawRectangle(self,WINDOW):
        pygame.draw.rect(WINDOW, self.colour, pygame.Rect(self.x, self.y, self.width, self.height))

#Functions for different events in the game and readability

def prepareGame():
    WINDOW.fill(WIN_COLOR)
    drawMainStreet()
    drawMiscellaneous()
    Shooting()
    characterCollisionHandler()
    textHandler()

def characterCollisionHandler():
    playerColl = pygame.rect.Rect(person.x,person.y,person.playerImg.get_width(),person.playerImg.get_height()) 
    enemyColl = pygame.rect.Rect(zombie.x,zombie.y,zombie.enemyImg.get_width(),zombie.enemyImg.get_height())

    playerColl.left = person.x
    enemyColl.top = person.y

    enemyColl.left = zombie.x
    enemyColl.top = zombie.y

    if pygame.Rect.colliderect(playerColl,enemyColl):
        LossState = True
        winOrLossState(LossState)

def winOrLossState(LossState):
    if winState: 
        textRect = UIFont.get_rect("YOU WIN!")
        UIFont.render_to(WINDOW, (WINDOW_WIDTH/2 - textRect.width/2, WINDOW_HEIGHT/2 - textRect.height/2), "YOU WIN!", GRAY)

    elif LossState: 
        textRect = UIFont.get_rect("GAME OVER!")
        UIFont.render_to(WINDOW, (WINDOW_WIDTH/2 - textRect.width/2, WINDOW_HEIGHT/2 - textRect.height/2), "GAME OVER!", GRAY, Size=100)


def drawMainStreet():
    building = DrawBackground(0,400,200,700,(127,127,127))
    oppositeBuilding = DrawBackground(1720,400,200,700,(127,127,127))
    topBuilding = DrawBackground(0,0,1920,100,(127,127,127))

    building.drawRectangle(WINDOW)
    oppositeBuilding.drawRectangle(WINDOW)
    topBuilding.drawRectangle(WINDOW)

def textHandler():
    UIFont.render_to(WINDOW, (10,10), "Score: "+str(score), (0, 0, 0),size=80)

def drawMiscellaneous():
    person.drawPlayer(WINDOW)
    zombie.drawEnemy(WINDOW)

def Shooting():
    for bullet in bulletList:
        bullet.drawBullet(WINDOW)
        bullet.shootBullet()

#Define characters and other properties in the game

#character variable init
person = Player(912,WINDOW_WIDTH/2,128,128)
zombie = Enemy(800,WINDOW_HEIGHT/2,128,128)
playerAlive = True

#Bullet variable init
bulletList = []
BULLET_TIME = 0.6
timeSinceFire = 0

#Win/Loss state variable init
score = 0
scoreToWin = 100
winState = False
LossState = False

#Text
UIFont = pygame.freetype.Font("Assets/Fonts/KenneyHighSquare.ttf",24)

#Main Game loop - stuff that will happen every game frame time

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

    if keys[pygame.K_SPACE] and timeSinceFire >= BULLET_TIME:
        bulletList.append(projectile(person.x+person.width//3,person.y+person.height//2,7,(255,255,0),6))
        timeSinceFire = 0
    
    timeSinceFire += frameSec

    prepareGame()
    pygame.display.update()

pygame.quit()