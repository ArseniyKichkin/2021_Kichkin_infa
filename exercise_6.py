import turtle as t
n = int(input('Введите количество лап' + '\n'))

t.shape("turtle")
t.color("blue")
t.width(2)

for i in range(n):
    t.forward(80)
    t.stamp()
    t.backward(80)
    t.left(180)
    t.left(180 * (n - 2) // n)
input()
