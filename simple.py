import json
import random
import sys
import sqlite3
from classes.Human import Human

def main():
	print("Welcome to my playground!")

	def shouldIplayWoW():
		print("no!")

	def classTierList():
		classDict = {"Death Knight": "B", "Demon Hunter": "C"}

		for k, tier in classDict.items():
			print(f"{k} is tier {tier}")

	# in python we call arrays lists
	def handlingArrays():
		groceries = ["apple", "orange", "banana"]
		for index, item in enumerate(groceries):
			print(f"item number {index +1} I need to buy a {item}")

	def optionalvalues(start, end, default=10):
		print(f"I am going to start count at {start} and I am going to finish at {end} but my default is {default}")
		for line in range(start, end, default):
			print(f"catchphrase")

	def showPeople():
		# what I want is this to print something like "This is Mr John doe and he works at <company> at <department>"
		with open("assets/data.json", "r", encoding='utf-8') as fileOutput:
			data = json.load(fileOutput)[:5]
			for person in data:
				print(f"This is {person['title']} {person['first_name']} {person['last_name']}, this person works at {person['company']} in {person['department']} and I am from {person['city']}, {person['country']}")
				#for information, value in person.items():
				#	print(f"{information}: {value}")

	# write something to json
	def tojson():
		todo = ["Homework", "Workout", "Eat healthy",]
		with open("assets/feed.json", "w") as file:
				json.dump(todo, file)

	def rng():
		for i in range(10):
			print(f"{random.randint(1,100)}")

	def attempts():
		target = 42
		guess =  0
		attempts = 0
		while guess != target:
			guess = random.randint(1,10000)
			attempts += 1
		print(f"Found {target} after {attempts} attempts!")

	def errorCodes(errors):
		match errors:
			case 100:
				return "Error!"
			case _:
				return "I don\'t know this error code"

	def shoppingList():
		shopping_list = {'fruit': ['Apple', 'Banana', 'Orange'], 'vegtable': ['Cabbage', 'Brocoli', 'paprika'], 'meat': ['chicken','turkey','rabbit']}
		for key, value in shopping_list.items():
			print(f'{key}')
			for sub_items in value:
				print(f'{sub_items}')

	# function calls
	print(f"I am running Python: {sys.version}")
	shouldIplayWoW()
	classTierList()
	handlingArrays()
	#optionalvalues(0, 10)
	# let's do something with JSON.
	showPeople()
	#tojson()
	# let's do something with random numbers
	rng()
	attempts()
	# Awesome we got Switch statements in Python now!
	print(f"This message is for error code: {errorCodes(100)}")
	shoppingList()

	# calling my class
	john = Human("john","Doe", 42)
	print(f'Hi my name is John and {john.returnAge()}')
	print(f'John, do you have a job? {john.employed()}')
	print(f'I have {len(john.list_hobbies())} hobbies')
	for hobby in john.list_hobbies():
		print(f'{hobby}, is a hobby of mine')
	print(f'In  3 years I will be making: {john.calculate_future_salary(5)} Euro')

	# container functions
	example_tuple = (1,2,3,4,5)
	reversed_tuple = reversed(example_tuple)

	print(f'{reversed_tuple}')
	# I can display this value in two different ways:
	for item in reversed_tuple:
		print(f'{item}', end=',')
	print('\n')
	print(f'{list(reversed(example_tuple))}')

	# zip function
	zip_numbers_one = (1, 2, 3, 4, 5)
	zip_numbers_two = (6, 7, 8, 9, 0)
	zip_result = zip(zip_numbers_one, zip_numbers_two)
	for k, v in zip_result:
		print(f'{k} - {v}')

	# enumarate 
	enumerate_items = ('orange', 'apple', 'banana', 'carrot', 'cucumber')
	for index, value in enumerate(enumerate_items):
		print(f'at index {index} we have: {value}')


if __name__ == "__main__":
	main()
