import random
from turtle import Turtle, Screen

colours = ["medium blue",
           "red",
           "coral",
           "orange",
           "gold",
           "turquoise",
           "pink"]
walk = [90, 180, 270, 360]

tim = Turtle()
tim.pensize(5)


def walk_fd(position):
    tim.right(position)
    tim.fd(30)


s = 1
while s != 90:
    walk_fd(random.choice(walk))
    tim.color(random.choice(colours))
    s += 1

screen = Screen()
screen.exitonclick()
