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
tim.pensize(2)
tim.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return tuple(f"{r, g, b}")


def walk_fd(position):
    tim.right(position)
    tim.fd(30)


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random.choice(colours))
        tim.circle(100)
        current_heading = tim.heading()
        tim.setheading(current_heading + size_of_gap)


draw_spirograph(5)

screen = Screen()
screen.exitonclick()
