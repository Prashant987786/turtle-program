import random
from turtle import Turtle, Screen


colours = [ "medium blue",
            "red",
            "coral",
            "orange",
            "gold",
            "turquoise",
            "pink"]

tim = Turtle()
tim.shape("triangle")
angle = 1
while angle != 360:
    for _ in range(angle):
        tim.fd(2)
        tim.right(1)
    tim.color(random.choice(colours))
    angle += 1

screen = Screen()
screen.exitonclick()
