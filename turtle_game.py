import random
from turtle import Turtle, Screen

colours = ["medium blue",
           "red",
           "coral",
           "orange",
           "gold",
           "turquoise",
           "pink"]
is_race_start = False
screen = Screen()
screen.setup(width=600, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="who is gonna win this race??"
                                                          "color : ")
turtle = []
tom = Turtle()
tom.hideturtle()
tom.penup()
tom.goto(x=250, y=-200)
tom.pendown()
tom.setheading(90)
tom.fd(400)

y_positions = [60, 30, 0, -30, -60, -90, -120]
for i in range(0, 6):
    tim = Turtle(shape="turtle")
    tim.penup()
    tim.color(colours[i])
    turtle.append(tim)
    tim.goto(x=-250, y=y_positions[i])

if user_bet:
    is_race_start = True

while is_race_start:
    for i in turtle:
        if i.xcor() > 230:
            is_race_start = False
            wining_color = i.pencolor()
            if user_bet == wining_color:
                print(f"you have won! the {wining_color} turtle is winner!")
            else:
                print(f"you have lost! the {wining_color} turtle is winner!")
        random_distance = random.randint(0, 10)
        i.fd(random_distance)


screen.listen()

screen.exitonclick()
