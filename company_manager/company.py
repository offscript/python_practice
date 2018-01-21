import employee

class Company():

	def __init__(self, revenue, employees):

		self.revenue = revenue

	def generate_wages(revenue):

		executive_wages = revenue * .01
		manager_wages = revenue .001
		human_resources_wages = revenue * .0005
		sales_associate_wages = revenue * .0003
		
'''
	def generate_employees(employees):


	def generate_executive():

		tom = employee.Executive(100000, "male", "black", 65, 20)


	def generate_managers():

	def generate human_resources():

	def generate_sales_associates():
'''	

tom = employee.Executive(100000, "male", "black", 65, 20)
print(tom.wage)