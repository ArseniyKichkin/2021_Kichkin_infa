import turtle

turtle.speed(10)
turtle.shape('turtle')


def circle(k):
    for i in range(180):
        turtle.forward(0.5 + 0.2 * k)
        turtle.left(2)


def circle_1(k):
    for i in range(180):
        turtle.forward(0.5 + 0.2 * k)
        turtle.right(2)


def butterfly():
    for i in range(10):
        circle(i)
        circle_1(i)
butterfly()

input()
