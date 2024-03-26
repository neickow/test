from turtle import *
from random import randint

c=['#B0E0E6', '#ADD8E6', '#87CEEB', '#00BFFF', '#1E90FF', '#6495ED']
s=[70, 45, 110, 50, 80, 63, 80, 45]
def f(n):
    pensize(n*4)
    if 3>n>6:
        color(c[randint(0, len(c) - 1)])
        dot(s[randint(0, len(s) - 1)])
        color('#191970')

    if n ==0:
        color(c[randint(0,len(c)-1)])
        dot(s[randint(0,len(s)-1)])
        color('#191970')
        return
    left(20)
    forward(30*n)
    f(n-1)
    pensize(n*4)
    backward(30*n)
    right(40)
    forward(30*n)
    f(n-1)
    pensize(n*4)
    backward(30*n)
    left(20)

tracer(1)
screensize(3000,3000)
left(90)
up()
backward(1000)
n=8
down()
color('#191970')
pensize((n+1)*4)
forward(30*(n+1))
f(n)

done()