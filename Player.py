import pygame
pygame.init()

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
    