import turtle

turtle.shape('turtle')
turtle.speed(0)
turtle.fillcolor('yellow')

turtle.begin_fill()
for i in range(180):
    turtle.forward(3)
    turtle.left(2)

turtle.end_fill()
turtle.penup()
turtle.goto(-40, 120)
turtle.pendown()

turtle.fillcolor('blue')
turtle.begin_fill()
for i in range(180):
    turtle.forward(0.4)
    turtle.left(2)
turtle.end_fill()

turtle.penup()
turtle.goto(40, 120)
turtle.pendown()
turtle.begin_fill()
for i in range(180):
    turtle.forward(0.4)
    turtle.left(2)
turtle.end_fill()

turtle.penup()
turtle.goto(0, 80)
turtle.pendown()

turtle.right(90)
turtle.color('black')
turtle.width(6)
turtle.forward(45)
turtle.penup()
turtle.goto(-60, 80)
turtle.pendown()

turtle.color('red')
turtle.width(8)
for i in range(90):
    turtle.forward(2)
    turtle.left(2)

input()