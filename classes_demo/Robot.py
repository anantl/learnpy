class Robot:

	population = 0;

	def __init__(self,name):
		print("Initialising robot {}".format(name))

		self.name = name
		print("Hi my name is {}".format(self.name))
		
		Robot.population += 1;
	
	def die(self):
		print("Killing off {}".format(self.name))
		Robot.population -= 1;

		if (Robot.population == 0):
			print("This was the last robot of its kind")
		else:
			print("There are a total of {} robots remaining".format(Robot.population))

	@classmethod
	def how_many(cls):
		print("There are a total of {} robots now".format(cls.population))

	def say_something(self):
		print("{} says something".format(self.name))

		

r2d2 = Robot("R2D2")
c3po = Robot("C3PO")
Robot.how_many()

r2d2.die()
c3po.die()
Robot.how_many()
