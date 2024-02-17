#PythonDraw.py
import turtle#引入海龟绘图体系
turtle.setup(650, 350, 200, 200)#引入一个窗体
turtle.penup()#将画笔抬起
turtle.fd(-250)#让海龟倒退向后行250个像素
turtle.pendown()#将画笔落下
turtle.pensize(25)#对画笔的尺寸进行设计，设定画笔像素为25
turtle.pencolor("purple")#笔的颜色为紫色
turtle.seth(-40)#将海龟方向改为绝对的-40度方向
for i in range(4):#运用sicle函数让海龟走曲线
    turtle.circle(40, 80)#使用40像素为半径绘制80度的弧度
    turtle.circle(-40, 80)#使用反向40像素为半径绘制80度的弧度
turtle.circle(40, 80/2)#以40度度的方向绘制小半个图形
turtle.fd(40)#向前行进40个像素
turtle.circle(16, 180)#使用半圆形绘制蟒蛇头部vvv
turtle.fd(40 * 2/3)#
turtle.done()#程序运行之后不会退出
