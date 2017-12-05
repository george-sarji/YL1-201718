from turtle import *
import random
import math

class Ball(Turtle):
	def __init__(self, radius, color, speed):
		Turtle.__init__(self)
		self.shape("circle")
		self.shapesize(radius/10)
		self.radius = radius
		self.color(color)
		self.speed(speed)

# Code to create two ball objects here
first_ball = Ball(10, "blue", 0)
second_ball = Ball(5, "red", 1)

def check_collision(ball1, ball2):
	# Logic to check if the balls collide.
	distance = math.sqrt(math.pow(ball1.xcor()-ball2.xcor(),2)+math.pow(ball1.ycor()-ball2.ycor(),2))
	radii_total = ball1.radius+ball2.radius
	# Alternative way of getting the radius:
	# radii_total = ball1.shapesize()[0]*10+ball2.shapesize()[0]*10
	if(distance<=radii_total):
		# Check which ball is bigger and make the smaller one teleport
		if(ball1.radius > ball2.radius):
			# Ball 2 gets teleported
			ball2.pu()
			ball2.ht()
			ball2.goto(random.randint(0, 1000), random.randint(0, 1000))
			print("Whoosh! A ball has teleported!")
			ball2.st()
			ball2.pd()
		elif(ball1.radius < ball2.radius):
			# Ball 1 gets teleported
			ball1.pu()
			ball1.ht()
			ball1.goto(random.randint(0, 1000), random.randint(0, 1000))
			print("Whoosh! A ball has teleported!")
			ball1.st()
			ball1.pd()
		else:
			# Teleport both balls
			ball1.pu()
			ball1.ht()
			ball1.goto(random.randint(0, 1000), random.randint(0, 1000))
			print("Whoosh! A ball has teleported!")
			ball1.st()
			ball1.pd()

			ball2.pu()
			ball2.ht()
			ball2.goto(random.randint(0, 1000), random.randint(0, 1000))
			print("Whoosh! A ball has teleported!")
			ball2.st()
			ball2.pd()


# Extra - Create a list of balls and make a while that always checks collisions

ballsList = []
ballsList.append(first_ball)
ballsList.append(second_ball)
ballsList.append(Ball(20, "purple", 0))

def check_collisions(ballsList):
	for ball1 in ballsList:
		for ball2 in ballsList:
			if(ball1!=ball2):
				check_collision(ball1, ball2)


