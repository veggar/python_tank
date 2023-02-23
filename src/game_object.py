import pygame
import math

DEFAULT_ENERGY:int = 100
DEFAULT_SIZE:int = 40

Bullets = []

class Tank:
    def __init__(self, name, cx=0, cy=0, color=pygame.Color(255,255,255)):
        self.reset(name, cx, cy, color)

    def reset(self, name, cx, cy, color):

        self.name = name
        self.color = color
        
        self.size = DEFAULT_SIZE

        self.surface = pygame.Surface([self.size, self.size])

        self.setPosition(cx,cy)        
        self.setAngle(0)

        self.setEnergy(DEFAULT_ENERGY)
        self.delete = False

    def setPosition(self, x, y):
        
        self.cx = x
        self.cy = y

    def addPosition(self, x, y):
        self.cx += x * math.sin(self.angle)
        self.cy -= y * math.cos(self.angle)

    def setAngle(self, angle):
        self.angle = angle

    def addAngle(self, angle):
        self.angle += angle

    def setEnergy(self, energy):
        self.energy = energy

    def render(self, display):
        window = display.window
        pygame.draw.rect(window, self.color, )
        return 
    def __str__(self):
        return "cx: {}, cy: {}, angle: {}, energy: {}, state: {}".format(self.cx, self.cy, self.angle, self.energy, self.delete)


class Bullet:
    def __init__(self, owner:Tank):
        self.reset(owner)

    def reset(self, owner:Tank):
        self.owner = owner
        self.color = owner.color
        self.x = owner.cx+20
        self.y = owner.cy+40
        self.angle = owner.angle
        self.delete = False

    def addPosition(self, x, y):
        self.x -= x * math.sin(self.angle)
        self.y += y * math.cos(self.angle)

    def __str__(self):
        return "x: {}, y:{}, angle: {}, owner: {}, state: {}".format(self.x, self.y, self.angle, self.owner.name, self.delete)

def createBullet(self, tank:Tank):
    for bullet in Bullets:
        if bullet.delete:
            bullet.reset(tank)
            return

    bullet = Bullet(tank)
    Bullets.append(bullet)

    print("create bullet of {}, length: {}".format(bullet.owner.name, len(Bullets)))

