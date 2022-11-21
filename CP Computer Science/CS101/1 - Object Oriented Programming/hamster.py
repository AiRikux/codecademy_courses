# Create your class here
class Hamster:
	# Create a __init__ method
	def __init__(self, input_name, input_breed, input_age=0, input_friendly=False):
		self.name = input_name
		self.breed = input_breed
		self.age = input_age  # in months
		self.friendly = input_friendly
		self.hungry = False
		self.steps = 0  # move count
		self.sleep = False

	# Create method to change
	# describe the hamster -- use repr for string outputs
	def __repr__(self):
		desc = f"{self.name} is a {self.breed} who is {self.age} months old."
		return desc
	# method when steps or move too much will make him hungry
	def hunger(self):
		if self.steps > 10:
			self.hungry = True

	# move method adding to the steps
	def move(self, step=1):
		self.steps += step

	# find out if the hamster is hungry
	def is_hungry(self):
		if self.hungry:
			print("The hamster is hungry! Give it food!!")
		else:
			print("The hamster is not hungry yet")


# Create a new pet!
bobinski = Hamster("Boba", "Syrian", 15, True)
print(bobinski)
bobinski.is_hungry()
