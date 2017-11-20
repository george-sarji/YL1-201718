from turtle import *
colormode(255)
import random


'''
class Square(Turtle):
    def __init__(self, size):
        Turtle.__init__(self)
        self.shapesize(size)
        self.shape("square")

    def random_color(self):
        r = random.randint(0, 256)
        g = random.randint(0, 256)
        b = random.randint(0, 256)
        self.color(r, g, b)
'''


class Rectangle(Turtle):
    def __init__(self, width, height, color, speed):
        Turtle.__init__(self)
        self.speed(speed)
        register_shape("Rectangle", ((0, 0), (0, height/2), (width/2, height/2), (width/2, -height/2), (-width/2, -height/2), (-width/2, height/2), (0, height/2), (0, 0)))
        self.shape("Rectangle")
        self.color(color)

    def random_color(self):
        r = random.randint(0, 256)
        g = random.randint(0, 256)
        b = random.randint(0, 256)
        self.color(r, g, b)
    
class Square(Rectangle):
    def __init__(self, size, color, speed):
        Rectangle.__init__(self, size, size, color, speed)

class Hexagon(Turtle):
    def __init__(self, size, color, speed):
        Turtle.__init__(self)
        self.begin_poly()
        for corner in range(6):
            self.forward(size)
            self.right(360/6)

        self.end_poly()
        register_shape("Hexagon", self.get_poly())
        self.shape("Hexagon")
        self.speed(speed)
        self.color(color)
        self.clear()

class Polygon(Turtle):
    def __init__(self, lines, speed, color):
        Turtle.__init__(self)
        self.begin_poly()
        for i in range(lines):
            self.forward(50)
            self.right(360/lines)
        self.end_poly()
        register_shape("poly"+str(lines), self.get_poly())
        self.shape("poly"+str(lines))
        self.color(color)
        self.speed(speed)

    def random_color():
        r = random.randint(0, 256)
        g = random.randint(0, 256)
        b = random.randint(0, 256)
        self.color(r, g, b)
            

square = Square(15, "red", 0)
rectangle = Rectangle(10, 20, "pink", 0)

hexagon = Hexagon(10, "purple", 0)
