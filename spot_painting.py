import random
from turtle import Turtle, Screen

colours = ["medium blue",
           "red",
           "coral",
           "orange",
           "gold",
           "turquoise",
           "pink"]

tim = Turtle()
tim.up()
tim.hideturtle()
tim.speed("fastest")
tim.setheading(225)
tim.fd(300)
tim.setheading(0)


def move_right():
    for _ in range(2):
        tim.right(90)
        tim.fd(30)


def move_left():
    for _ in range(2):
        tim.left(90)
        tim.fd(30)


for _ in range(7):
    for _ in range(14):
        tim.dot(10, random.choice(colours))
        tim.fd(30)
    move_left()
    for _ in range(14):
        tim.dot(10, random.choice(colours))
        tim.fd(30)
    move_right()

screen = Screen()
screen.exitonclick()
