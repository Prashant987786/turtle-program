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
screen = Screen()


def move():
    tim.fd(10)


def clear_screen():
    tim.clear()


def move_forward():
    tim.fd(10)


def move_backward():
    tim.bk(10)


def move_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)
    tim.fd(10)


def move_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)
    tim.fd(10)


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="space", fun=move)
screen.onkey(key="c", fun=clear_screen)
screen.exitonclick()
