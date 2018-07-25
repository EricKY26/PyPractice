abs(100)
abs(-15)
abs(1.356)

a = -7.256
abs_a = abs(a)

max(1, 2, 3.58, -9, 100)

n1=255
n2=1000
n1_16=hex(n1)
n2_16=hex(n2)
print('n1 = '+n1_16)
print('n2 = '+n2_16)


def nop():
    pass

age=int(input('Please input your age: '))
if age>=18:
    pass

import math

def move(x,y,step,angel=0):
    nx=x+step*math.cos(angel)
    ny=y+step*math.sin(angel)
    return nx,ny

