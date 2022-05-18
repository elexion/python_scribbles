import json
import math

class Human:
	print('I am the human class')
	# int
	age = 0
	# float
	length = 1.88
	hair_color = 'Brown'

	base_salary = 25000.00

	# bool
	job = False
	# empty string
	job_title = ''

	# list
	hobbies =  ['walking', 'eating', 'laughing']
	
	# dictionaries
	friends = {}
	disliked_people = {"": ""}

	def __init__(self, firstname, lastname, age):
		self.firstname = firstname
		self.lastname = lastname
		self.age = age

	def returnAge(self):
		return f'I am {self.age} years old'

	def employed(self):
		if(self.job):
			return 'I have a job'
		else:
			return 'I suck, I don\'t have a job'

	def list_hobbies(self):
		return self.hobbies
		#for hobby in self.hobbies:
		#	return f'{hobby} is a hobby of mine'

	def calculate_future_salary(self, years_employed):
		future_salary = self.base_salary * 0.25
		result = self.base_salary + future_salary
		return result