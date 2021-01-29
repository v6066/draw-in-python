#绘制椭圆
from turtle import*
pendown()
setheading(90)
len=1
for k in range(2):
    for j in range(60):
        if j<30:
            len+=0.2
        else:
            len-=0.2
        fd(len)
        left(3)
penup()
down()
