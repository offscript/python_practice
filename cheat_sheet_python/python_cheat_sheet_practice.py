'''
#Printing
msg = "Hello World"
print(msg)
first_name = 'Thomas'
last_name = 'Keating'

bikes = [first_name, last_name]

#Generating lists 1
print(bikes[0] + bikes[1])
bikes.append('monkey')
print(bikes)

numbers = []
for x in range(1,12):
  numbers.append(x**2)
  
print(numbers)

#Generating Lists 2
comprehended_numbers = [x**2 for x in range(1, 11)]
print(comprehended_numbers)

finishers = ['sam', 'bob', 'ada', 'bea']
first_two = finishers[:2]
print(finishers[1:3])

#Tuples
const = (1,2,3)
print(const[1])

outdoors = ['mountains', 'ocean', 'sky', 'animals']
print("heater" in outdoors)
print("comfort" not in outdoors)
'''

degrees_outside_Fahrenheit = 30

if degrees_outside_Fahrenheit > 32:
	print("It's only brisk!")
else:
	print("Ok it's a bit chilly, no?")




