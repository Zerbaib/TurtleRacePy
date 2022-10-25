from turtle import *
from random import randint

ada = Turtle()
ada.color('red')
ada.shape('turtle')
ada.penup()
ada.goto(-160, 100)
ada.pendown()

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
    ada.forward(randint(1,5))
    bob.forward(randint(1,5))
    kevin.forward(randint(1,5))
    patrik.forward(randint(1,5))
