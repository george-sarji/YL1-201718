# Problem 1
print("George")

print("George "*3)

print("George "*100)

# Problem 2
number1 = 15

print(number1)
number2=number1/2

print(number2)

# Problem 3
mylist=[15, 205, 123]
sum=0
for value in mylist:
    print(value)
    print(value*2)
    sum+=value

# Problem 4

import turtle
turtle.pu()
turtle.goto(100, 100)
turtle.pd()
turtle.goto(0, 100)
turtle.goto(0, 0)
turtle.goto(100, 0)
turtle.goto(100, 100)
turtle.pu()

turtle.reset()

# Extra
turtle.speed(0)
turtle.pensize(10)

turtle.pu()
turtle.pencolor("blue")
turtle.goto(-100, 0)
turtle.pd()
turtle.circle(50)

turtle.pu()
turtle.pencolor("yellow")
turtle.goto(-50, 50)
turtle.pd()
turtle.right(180)
turtle.circle(50)

turtle.pu()
turtle.pencolor("black")
turtle.goto(0, 0)
turtle.pd()
turtle.right(180)
turtle.circle(50)

turtle.pu()
turtle.pencolor("green")
turtle.goto(50, 50)
turtle.pd()
turtle.right(180)
turtle.circle(50)

turtle.pu()
turtle.pencolor("red")
turtle.goto(100, 0)
turtle.right(180)
turtle.pd()
turtle.circle(50)

turtle.mainloop()
