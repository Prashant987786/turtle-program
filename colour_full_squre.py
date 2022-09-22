
import turtle

colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
t = turtle.Pen()
t.speed("fastest")
turtle.bgcolor('black')
for x in range(360):
    t.pencolor(colors[x % 5])
    t.width(x // 100 + 1)
    t.forward(x)
    t.left(91)
screen = turtle.Screen()
screen.exitonclick()
