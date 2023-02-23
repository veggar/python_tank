import time

import pygame
import game_object


# reference for https://github.com/nicostudt/PiTable/blob/b73681c1508b8099713252a47f60f06d04e7300a/engine/engine.py

Tanks = []

def init():
    Tanks.append(game_object.Tank("tank 1", 50, 50, pygame.Color(0, 0, 255)))
    return

def process(event, inverval_ms=33):

    if event != None and event.type == pygame.KEYDOWN:
        
        print("event {}:{}".format(event.type, event.key))

        match int(event.key):
            case pygame.K_q: # change the value to False, to exit the main loop
               return False
            case pygame.K_d:
                render(None)
            case pygame.K_UP:
                Tanks[0].addPosition(-5,-5)
            case pygame.K_DOWN:
                Tanks[0].addPosition(5,5)
            case pygame.K_LEFT:
                Tanks[0].addAngle(-0.1)
            case pygame.K_RIGHT:
                Tanks[0].addAngle(0.1)
            case _:
                pass
                

    return True

def control_input(key):
    return

def render(display):
    if len(Tanks) > 0:
        print(Tanks[0])
    for obj in Tanks:
        obj.render(display)
    return

def quit():
    return