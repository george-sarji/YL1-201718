import turtle
import time
import random
from Ball import *
import math

turtle.hideturtle()
RUNNING = True
SLEEP = 0.0077
SCREEN_WIDTH = turtle.getcanvas().winfo_width()/2
SCREEN_HEIGHT = turtle.getcanvas().winfo_height()/2

# Part 0

MY_BALL = Ball(50, 50, 0 ,0 ,50, "yellow")

NUMBER_OF_BALLS = 5
MINIMUM_BALL_RADIUS = 10
MAXIMUM_BALL_RADIUS = 100
MINIMUM_BALL_DX = -5
MAXIMUM_BALL_DX = 5
MINIMUM_BALL_DY = -5
MAXIMUM_BALL_DY = 5

BALLS = []

for index in range(NUMBER_OF_BALLS):
	x = random.randint(int(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS), int(SCREEN_WIDTH - MAXIMUM_BALL_RADIUS))
	y = random.randint(int(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS), int(SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS))
	dx = random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
	dy = random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DY)
	radius = random.randint(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS)
	color = "blue"
	print("Added ball "+str(index))
	print("radius: "+str(radius))
	print("X" + str(x))
	print("Color: ")
	print(color)
	BALLS.append(Ball(x, y, dx, dy, radius, color))


# Part 1

def move_all_balls():
	for ball in BALLS:
		ball.move(SCREEN_WIDTH, SCREEN_HEIGHT)


# Part 2

def collide(ball_a, ball_b):
	if(ball_a == ball_b):
		return False
	distance = math.sqrt(math.pow(ball_a.xcor()-ball_b.xcor(), 2)+math.pow(ball_a.ycor()-ball_b.ycor(), 2))
	return distance+10<=ball_a.r+ball_b.r

# Part 3

def check_all_balls_collision():
	for ball_a in BALLS:
		for ball_b in BALLS:
			if(collide(ball_a, ball_b)):
				radius_a = ball_a.r
				radius_b = ball_b.r
				x = random.randint(int(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS), int(SCREEN_WIDTH - MAXIMUM_BALL_RADIUS))
				y = random.randint(int(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS), int(SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS))
				dx = random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
				dy = random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DY)
				while(dx == 0):
					dx = random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
				while(dy==0):
					dy = random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DY)
				radius = random.randint(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS)
				color = (random.random(), random.random(), random.random())

				if(radius_a<radius_b):
					smaller_ball = ball_a
					bigger_ball = ball_b
				else:
					smaller_ball=ball_b
					bigger_ball = ball_a
				smaller_ball.goto(x, y)
				smaller_ball.dx=dx
				smaller_ball.dy=dy
				smaller_ball.r=radius
				smaller_ball.shapesize(radius/10)
				smaller_ball.color(color)
				bigger_ball.r+=1
				bigger_ball.shapesize(bigger_ball.r/10)

# Part 4

def check_myball_collision():
	for ball in BALLS:
		if(collide(MY_BALL, ball)):
			ball_radius = ball.r
			my_radius = MY_BALL.r
			if(my_radius<ball_radius):
				print("False")
				return False
			else:
				x = random.randint(int(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS), int(SCREEN_WIDTH - MAXIMUM_BALL_RADIUS))
				y = random.randint(int(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS), int(SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS))
				dx = random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
				dy = random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DY)
				while(dx == 0):
					dx = random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
				while(dy==0):
					dy = random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DY)
				radius = random.randint(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS)
				color = (random.random(), random.random(), random.random())
				ball.goto(x, y)
				ball.dx=dx
				ball.dy=dy
				ball.r=radius
				ball.shapesize(radius/10)
				ball.color(color)
				MY_BALL.r+=1
				MY_BALL.shapesize(MY_BALL.r/10)
	print("True")
	return True

# Part 5

def movearound(event):
	MY_BALL.goto(event.x - SCREEN_WIDTH, SCREEN_WIDTH + event.y)

# Part 5.1

turtle.getcanvas().bind("<Motion>", movearound)
turtle.listen()



while RUNNING:
	if(SCREEN_WIDTH != turtle.getcanvas().winfo_width()/2 or SCREEN_HEIGHT != turtle.getcanvas().winfo_height()/2):
		SCREEN_WIDTH = turtle.getcanvas().winfo_width()/2
		SCREEN_HEIGHT = turtle.getcanvas().winfo_height()/2
	move_all_balls()
	check_all_balls_collision()
	MY_BALL.move(SCREEN_WIDTH, SCREEN_HEIGHT)
	RUNNING = check_myball_collision()
	time.sleep(SLEEP)
		
mainloop()