﻿# -*- coding:utf-8 -*-

import pyglet
from pyglet.window import mouse
from GameModules.gamebox import Box
from GameModules.gamemap import *
from GameModules.loadobj import boxes
import math

initCoord = [-1,-1]
#保存初始坐标
def mouseCoord(*args):
    px = args[0]
    py = args[2]

    initCoord[0] = px
    initCoord[1] = py

#获取鼠标拖动方向
def mouseDrag(*args):
    dx = args[1] - args[0]
    dy = args[3] - args[2]

    def sin(x, y):
        try:
            return(y / math.sqrt(x**2 + y**2))
        except(ZeroDivisionError):
            pass

    sinM = sin(dx, dy)

    if sinM == None:
        dragCoord = -1
    elif sinM > 1/math.sqrt(2):
        dragCoord = 2
    elif sinM < -1/math.sqrt(2):
        dragCoord = 4
    elif dx > 0:
        dragCoord = 1
    else:
        dragCoord = 3
    boxID = getBoxID(initCoord)
    print boxID

    dragBox(boxID,dragCoord)
    
    boxes.threeMoreDeath(4,0)
    boxes.moveAllDown()
    boxes.initBoxCounter()
    print boxes.boxArray

def getBoxID(args):
    m = (args[1] - MARGINLOW - BORDER + 0.5 * Box.BOXSIZE + Box.PADDING) / (Box.BOXSIZE + Box.PADDING)
    n = (args[0] - MARGINLEFT - BORDER + 0.5 * Box.BOXSIZE + Box.PADDING) / (Box.BOXSIZE + Box.PADDING)
    
    return (int(round(m))-1,int(round(n))-1)

def dragBox(boxID, dragCoord):
    try:
        if boxes.boxArray[boxID[0]][boxID[1]] != 2:
            if dragCoord == -1:
                pass
            elif dragCoord == 1:
                boxes.swap(boxID, (boxID[0], boxID[1] + 1))
            elif dragCoord == 2:
                boxes.swap(boxID, (boxID[0] + 1, boxID[1]))
            elif dragCoord == 3:
                boxes.swap(boxID, (boxID[0], boxID[1] - 1))
            elif dragCoord == 4:
                boxes.swap(boxID, (boxID[0] - 1, boxID[1]))
    except(IndexError):
        pass



    #for i in boxes:
    #    for j in i:
    #        if j.
    