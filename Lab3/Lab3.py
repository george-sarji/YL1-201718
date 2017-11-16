import turtle

def make_shape():
	turtle.forward(200)
	turtle.right(45)
	turtle.forward(100)
	turtle.right(90)
	turtle.forward(50)
	turtle.right(45)
	
turtle.speed(0)
for index in range(540):
	make_shape()
	turtle.pu()
	turtle.goto(0,0)
	turtle.pd()
	turtle.right(0.3)
	
	
turtle.mainloop()
