"""Turtle tutorial."""

from turtle import Turtle, colormode, done
colormode(255)
leo: Turtle = Turtle()

leo.penup()
leo.goto(-5, 0)
leo.pendown()

leo.color((130, 22, 22), (245, 199, 125))

leo.speed(50)
leo.begin_fill()
i: int = 0
while (i < 3):
    leo.forward(300)
    leo.left(120)
    i = i + 1
leo.end_fill()
leo.hideturtle()

bob: Turtle = Turtle()

bob.penup()
bob.goto(-70, -30)
bob.pendown()

bob.color(0, 0, 0)

bob.speed(100)

c: int = 0
while (c < 3):
    bob.forward(400)
    bob.left(120)
    c = c + 1

side_length: int = 300

i: int = 0
while (c < 3):
    bob.forward(600)
    bob.left(122)
    i = i + 1
    side_length = side_length * int(0.97)

done()