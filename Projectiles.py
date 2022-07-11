import pygame
pygame.init()

class projectile(object):
    def __init__(self, bulletx, bullety, radius, colour, width):
        self.bulletx = bulletx
        self.bullety = bullety
        self.radius = radius
        self.colour = colour
        self.width = width
        self.velocity = 400

    def drawBullet(self, WINDOW):
        pygame.draw.circle(WINDOW, self.colour, (self.bulletx, self.bullety), self.radius, self.width)
    
    def shootBullet(self):
        self.bullety -= self.velocity * frameSec