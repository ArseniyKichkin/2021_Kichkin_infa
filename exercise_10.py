import turtle as t

t.speed(0)
t.shape('turtle')


def left():
    for i in range(180):
        t.forward(2)
        t.left(2)


def right():
    for i in range(180):
        t.forward(2)
        t.right(2)


left()
right()
t.left(60)
left()
right()
t.left(60)
left()
right()

input()
