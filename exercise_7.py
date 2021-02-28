import turtle as t
t.shape('turtle')
t.speed(20)
t.color('blue')
t.width(2)
for i in range(1000):
    t.forward(i * 0.001)
    t.left(1)