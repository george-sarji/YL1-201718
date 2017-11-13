import turtle

# Exercise one

for i in range(5):
    turtle.forward(100)
    turtle.right(144)

# Exercise two

turtle.reset()
turtle.begin_fill()
turtle.goto(25, 0)
turtle.goto(25, -50)
turtle.goto(0, -75)
turtle.goto(-25, -50)
turtle.goto(-25, 0)
turtle.goto(0, 0)
turtle.end_fill()

turtle.register_shape("Pointer", ((25, 0), (25, -50), (0, -75), (-25, -50), (-25, 0), (0, 0)))
turtle.shape("Pointer")
