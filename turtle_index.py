import turtle
import math


def print0():
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(40)
    turtle.left(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(40)
    turtle.left(90)
    turtle.penup()
    turtle.forward(40)
    turtle.pendown()


def print1():
    turtle.penup()
    turtle.left(90)
    turtle.forward(20)
    turtle.pendown()
    turtle.right(45)
    turtle.forward(20 * math.sqrt(2))
    turtle.right(135)
    turtle.forward(40)
    turtle.left(90)
    turtle.penup()
    turtle.forward(20)
    turtle.pendown()


def print2():
    turtle.penup()
    turtle.left(90)
    turtle.forward(40)
    turtle.pendown()
    turtle.right(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(20)
    turtle.right(45)
    turtle.forward(20 * math.sqrt(2))
    turtle.left(135)
    turtle.forward(20)
    turtle.penup()
    turtle.forward(20)
    turtle.pendown()


def print3():
    turtle.left(45)
    turtle.forward(20 * math.sqrt(2))
    turtle.left(135)
    turtle.forward(20)
    turtle.right(135)
    turtle.forward(20 * math.sqrt(2))
    turtle.left(135)
    turtle.forward(20)
    turtle.penup()
    turtle.left(90)
    turtle.forward(40)
    turtle.left(90)
    turtle.forward(40)
    turtle.pendown()


def print4():
    turtle.penup()
    turtle.forward(20)
    turtle.left(90)
    turtle.pendown()
    turtle.forward(40)
    turtle.left(180)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(20)
    turtle.penup()
    turtle.left(180)
    turtle.forward(40)
    turtle.left(90)
    turtle.forward(40)
    turtle.pendown()


def print5():
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(20)
    turtle.penup()
    turtle.right(90)
    turtle.forward(40)
    turtle.left(90)
    turtle.forward(20)
    turtle.pendown()


def print6():
    turtle.left(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(20)
    turtle.right(45)
    turtle.forward(20 * math.sqrt(2))
    turtle.right(135)
    turtle.penup()
    turtle.forward(40)
    turtle.left(90)
    turtle.forward(20)
    turtle.pendown()


def print7():
    turtle.penup()
    turtle.left(90)
    turtle.forward(40)
    turtle.right(90)
    turtle.pendown()
    turtle.forward(20)
    turtle.right(135)
    turtle.forward(20 * math.sqrt(2))
    turtle.left(45)
    turtle.forward(20)
    turtle.penup()
    turtle.left(90)
    turtle.forward(40)
    turtle.pendown()


def print8():
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(40)
    turtle.left(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(40)
    turtle.left(180)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.penup()
    turtle.forward(20)
    turtle.pendown()


def print9():
    turtle.left(45)
    turtle.forward(20 * math.sqrt(2))
    turtle.left(45)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.penup()
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(20)
    turtle.pendown()


A = str(input())
i = 0
turtle.penup()
turtle.goto(-300, 0)
turtle.pendown()

while i < len(A):
    if A[i] == '0':
        print0()
    elif A[i] == '1':
        print1()
    elif A[i] == '2':
        print2()
    elif A[i] == '3':
        print3()
    elif A[i] == '4':
        print4()
    elif A[i] == '5':
        print5()
    elif A[i] == '6':
        print6()
    elif A[i] == '7':
        print7()
    elif A[i] == '8':
        print8()
    elif A[i] == '9':
        print9()
    i = i + 1
input()
