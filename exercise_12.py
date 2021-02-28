import turtle

turtle.speed(0)
turtle.shape('turtle')

turtle.left(90)
i = 0

while i < 4:
    n = 0
    while n < 180:
        turtle.forward(1)
        turtle.right(1)
        n = n + 1
    n = 1
    while n < 180:
        turtle.forward(0.15)
        turtle.right(1)
        n = n + 1
    i = i + 1

input()
