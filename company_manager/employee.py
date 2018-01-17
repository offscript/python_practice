class Employee():
	'''This is the base Employee class'''

	def __init__(self, wage, gender, race, age, experience):
		'''Here we initialize the employee'''
		self.wage = wage
		self.gender = gender
		self.race = race
		self.age = age
		self.experience = experience
'''
class Executive(Employee):

	def __init__(self, wage, gender, race, age, experience):
		'''Here we initialize the Executive'''
		super().__init__(wage, gender, race, age, experience)
		
		self.wage = wage
		self.gender = gender
		self.race = race
		self.age = age
		self.experience = experience
'''