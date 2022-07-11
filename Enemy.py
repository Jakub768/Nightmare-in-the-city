import pygame
pygame.init()

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
