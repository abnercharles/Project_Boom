﻿# -*- coding:utf-8 -*-
import pyglet

#定义常量
MARGINLOW = 30
MARGINHIGH = 30
MARGINLEFT = 40
BORDER = 20
BOARDSIZE = 540


# 0 -> empty, 1 -> box, 2 -> blocked
MAPARRAY1 = [[2,2,2,2,0,2,2,2,2],
             [2,2,2,0,0,0,2,2,2],
             [2,2,0,0,0,0,0,2,2],
             [2,0,0,0,0,0,0,0,2],
             [0,0,0,0,0,0,0,0,0],
             [2,0,0,0,0,0,0,0,2],
             [2,2,0,0,0,0,0,2,2],
             [2,2,2,0,0,0,2,2,2],
             [2,2,2,2,0,2,2,2,2]]
OBJIN1 = (8,4) #方块进入的坐标

BOXIDARRAY = list((i,j) for i in range(9) for j in range(9))
#REMOVEPOINTS = [(0,0), (0,1), (1,0), (0,8), (0,9), (5,8), (5,9)]
#for i in REMOVEPOINTS:
#    BOXIDARRAY.remove(i)

#B  OXIDITERATOR = iter(BOXIDARRAY)