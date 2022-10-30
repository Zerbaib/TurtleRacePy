from turtle import *
from random import randint

hugo = Turtle()
hugo.color('red')
hugo.shape('turtle')
hugo.penup()
hugo.goto(-160, 100)
hugo.pendown()

bob = Turtle()
bob.color('blue')
bob.shape('turtle')
bob.penup()
bob.goto(-160, 70)
bob.pendown()

kevin = Turtle()
kevin.color('green')
kevin.shape('turtle')
kevin.penup()
kevin.goto(-160, 40)
kevin.pendown()

patrik = Turtle()
patrik.color('yellow')
patrik.shape('turtle')
patrik.penup()
patrik.goto(-160, 10)
patrik.pendown()

speed(10)
penup()
goto(-140, 140)

for step in range(15):
    write(step, align='center')
    right(90)
    forward(10)
    pendown()
    forward(150)
    penup()
    backward(160)
    left(90)
    forward(20)

for turn in range(100):
    hugo.forward(randint(1,5))
    bob.forward(randint(1,5))
    kevin.forward(randint(1,5))
    patrik.forward(randint(1,5))
