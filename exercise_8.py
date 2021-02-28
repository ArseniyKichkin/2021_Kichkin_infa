import turtle as t

t.shape('turtle')
t.color('blue')
t.width(2)
t.speed(8)
count = 0
for i in range(0, 100, 10):
    t.forward(10 + count)
    t.left(90)
    t.forward(20 + count)
    t.left(90)
    t.forward(30 + count)
    t.left(90)
    t.forward(40 + count)
    t.left(90)
    count = 40 + count
input()
