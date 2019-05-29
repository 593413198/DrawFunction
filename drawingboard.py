#!/usr/bin/python3
# @brief: 一个自动画函数图形的脚本，展示画图过程
# @envir: linux, python3, pyautogui, tkinter
# @author: luhao
# @date: 2019,5,28

from tkinter import *

window = Tk()
window.title('Auto Drawing')
window.geometry('1000x800')

canvas = Canvas(window, bg='white')

width = 2 #画笔粗细
color = 'black' #画笔颜色
X, Y = IntVar(), IntVar() #记录落笔的坐标

def onLeftDown(event):
    X.set(event.x)
    Y.set(event.y)

def onLeftMove(event):
    canvas.create_line(X.get(), Y.get(), event.x, event.y, width=width, fill=color)
    X.set(event.x)
    Y.set(event.y)

canvas.bind('<Button-1>',onLeftDown) #单击鼠标左键
canvas.bind('<B1-Motion>',onLeftMove) #按住鼠标左键
#canvas.bind('<ButtonRelease-1>',onLeftUp) #松开鼠标左键
canvas.bind()
canvas.pack(fill=BOTH, expand=YES)
if __name__ == '__main__':
    window.mainloop()
