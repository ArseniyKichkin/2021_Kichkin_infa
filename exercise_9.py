import turtle
import math

turtle.shape('turtle')
turtle.speed(1)
n = 3
r = 10


def draw(n, m):
    q = 360 / n
    for i in range(n):
        turtle.left(q)
        turtle.forward(m)


for i in range(3, 14):
    m = 2 * r * math.sin(math.pi / i)  # считаем размер стороны многоугольника (a=2*R*sin (360/2n))
    x = (180 - 360 / i) / 2
    turtle.left(x)

    draw(i, m)
    turtle.right(x)
    turtle.penup()
    turtle.forward(10)

    turtle.pendown()

    r += 10
