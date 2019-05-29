### tkinter+pyautogui实现一个自动画函数图像的小程序

**编译环境：**
`linux + python3 + tkinter + pyautogui`

**创建时间：**
`2019,5,28`

**实现功能：**
- 画布界面采用tkinter下的canvas实现，绘图通过pyautogui对鼠标的操控实现
- 绘制f=a0+a1*x+a2*x^2+....+an*x^n的图像
- 绘制(a,b)为圆心，r为半径的圆

```python
draw_func(a0, a1, a2, ..., an)
draw_circle(a,b,r)
```
