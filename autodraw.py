#!/usr/bin/python3
# @brief: 一个自动画函数图形的脚本，展示画图过程
# @envir: linux, python3, pyautogui, tkinter
# @author: luhao
# @date: 2019,5,28

import pyautogui as gui
import numpy
from math import *

x1, y1 = 120, 120 #左上角坐标
x2, y2 = 1100, 900 #右下角坐标
x0, y0 = 610, 510 #中心坐标
t = 0.25
T = 0.001 #代表作图速度
mm = 50 #mm像素代表一个单位

def draw_coords():
    #　先画一个坐标系
    gui.moveTo(x1+20,y0)
    gui.dragTo(x2,y0,duration=t)
    gui.mouseUp() #松开鼠标
    gui.moveTo(x0,y2)
    gui.dragTo(x0,y1)
    gui.mouseUp()
    #　标一下最小单位
    _max = abs((x1-x0))/mm #　最大刻度数
    for i in range(int(_max)):
        gui.moveTo(x0+mm*i, y0)
        gui.dragTo(x0+mm*i, y0-5)
        gui.mouseUp()

def onScreen(x,y):
    #　判断要画的点是否在画布范围上
    if gui.onScreen(x,y) and x1<x<x2 and y1<y<y2:
        return True
    return False

def Draw(x,y):
    global first, last
    if not onScreen(x,y):
        last = True
        return 
    if first:
        gui.moveTo(x,y,duration=T)
        first = False
    if last:
        gui.moveTo(x,y,duration=T)
        last = False
    gui.dragTo(x,y)
    gui.mouseUp()

first = True
last = False # 记录上一个画点是否在画布外

def draw_func(*args):
    #　画F=a0 + a1x^1 + a2x^2 + ... + anx^n
    global first, last
    first = True
    last = False
    l = len(args)
    for i in numpy.arange(-20,21,0.1):
        j = 0
        for k in range(l):
            j += args[k]*(i**k)
        x, y = x0+mm*i, y0-mm*j
        Draw(x,y)

def draw_circle(X,Y,r):
    #　用参数方程画圆
    global first, last
    first = True
    last = False
    for i in range(0,361,1):
        x1 = r * sin(i/180*pi)
        y1 = r * cos(i/180*pi)
        x, y = x0+mm*X+mm*x1, y0-mm*Y-mm*y1
        Draw(x,y)

if __name__ == '__main__':
    draw_coords()
    draw_circle(1,1,2)
    draw_func(0,0,0,1)
    draw_func(0,0,1)
