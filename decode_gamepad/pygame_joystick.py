#!/usr/bin/python

import pygame
import time

def keyMap(e):
    if e.type == pygame.JOYAXISMOTION:
        if (e.dict['axis'] == 0):
            if (e.dict['value']<0):
                print "Going Left!"

            if (e.dict['value']>0):
                print "Going Right!"

        if (e.dict['axis'] == 1):
            if (e.dict['value']<0):
                print "Going Forward!"

            if (e.dict['value']>0):
                print "Going Backward!"


    elif e.type == pygame.JOYBUTTONDOWN:
        if (e.dict['button'] == 10):
            print "Stop"


pygame.init()
js = pygame.joystick.Joystick(0)
js.init()
while True:
    e = pygame.event.wait()
    if (e.type == pygame.JOYAXISMOTION or e.type == pygame.JOYBUTTONDOWN):
        keyMap(e)