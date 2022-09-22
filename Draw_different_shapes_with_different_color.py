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
screen.colormode(255)
screen.setup(width=600, height=600)
tim.shape("triangle")
tim.penup()
tim.goto(x=-50, y=300)
tim.pendown()
angle = 3
while angle != 16:
    for _ in range(angle):
        movement = 360 / angle
        tim.fd(100)
        tim.right(movement)
    tim.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    angle += 1

screen.exitonclick()
