class Animal(object):
	def __init__(self, sound, name, age, favorite_color):
		self.sound=sound
		self.name=name
		self.age = age
		self.favorite_color = favorite_color
		
	def eat(self, food):
		print("Yummy!! "+self.name+" is eating "+food)
		
	def description(self):
		print(self.name + " is "+ str(self.age) + " years old and loves the color "+self.favorite_color)
	
	def make_sound(self, x):
		print((self.sound+" ")*x)
		
	
		
# Problem 1
myAnimal = Animal("Skrra", "Big Shaq", 21, "Red")
myAnimal.eat("Carrots")
myAnimal.description()

myAnimal.make_sound(3)

# Problem 3
class Person(object):
	def __init__(self, name, age, city, gender, favorite_food, favorite_sport):
		self.name=name
		self.age=age
		self.city=city
		self.gender=gender
		self.favorite_food=favorite_food
		self.favorite_sport=favorite_sport
		
	def eat_breakfast(self):
		print(self.name + " is eating his breakfast, "+self.favorite_food)
		
	def play_sport(self):
		print("Wow! "+self.name+" is being useful and is playing "+self.favorite_sport)
		
randomPerson = Person("Test", 15, "Nazareth", "Male", "Apples", "Tennis")
randomPerson.eat_breakfast()
randomPerson.play_sport()


class Song(object):
	def __init__(self, lyrics):
		self.lyrics=lyrics
		
	def sing_me_a_song(self):
		for line in self.lyrics:
			print(line)
			
mySong = Song(["Ross are red", "Violets are blue", "I wrote this poem especially for you"])

mySong.sing_me_a_song()
