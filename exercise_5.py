import turtle as t

t.width(2)
t.color('blue')
t.shape('turtle')
for i in range(10):
    t.goto(-10*i, -10*i)
    t.pendown()
    t.forward(20 + 20*i)
    t.left(90)
    t.forward(20 + 20*i)
    t.left(90)
    t.forward(20 + 20*i)
    t.left(90)
    t.forward(20 + 20*i)
    t.left(90)
    t.penup()
input()
