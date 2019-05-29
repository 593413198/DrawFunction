### tkinter+pyautogui实现一个自动画函数图像的小程序
![在这里插入图片描述](https://img-blog.csdnimg.cn/20190529202529162.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2x1aGFvMTk5ODA5MDk=,size_2,color_FFFFFF,t_70)

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
