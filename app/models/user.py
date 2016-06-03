""" 
	Sample Model File

	A Model should be in charge of communicating with the Database. 
	Define specific model method that query the database for information.
	Then call upon these model method in your controller.

	Create a model using this template.
"""
from system.core.model import Model
import re
from time import strftime


class user(Model):
	def __init__(self):
		super(user, self).__init__()
		
	def create_user(self, user_info):
			# We write our validations in model functions.
			# They will look similar to those we wrote in Flask
			EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')
			regis_errors = []
			password = user_info['password']
			# Some basic validation
			if not user_info['first_name']:
				regis_errors.append('First name cannot be blank')
			elif len(user_info['first_name']) < 2:
				regis_errors.append('First name must be at least 2 characters long')
			if not user_info['last_name']:
				regis_errors.append('Last name cannot be blank')
			elif len(user_info['last_name']) < 2:
				regis_errors.append('Last name must be at least 2 characters long')
			if not user_info['email']:
				regis_errors.append('Email cannot be blank')
			elif not EMAIL_REGEX.match(user_info['email']):
				regis_errors.append('Invalid email format!')
			if not user_info['password']:
				regis_errors.append('Password cannot be blank')
			elif len(user_info['password']) < 8:
				regis_errors.append('Password must be at least 8 characters long')
			elif user_info['password'] != user_info['pw_confirmation']:
				regis_errors.append('Password and confirmation must match!')
			# If we hit errors, return them, else return True.
			if regis_errors:
				return {"status": False, "regis_errors": regis_errors}
			else:
				# Code to insert user goes here...
				pw_hash = self.bcrypt.generate_password_hash(password)
				query = "INSERT INTO users (first_name, last_name, email, password, created_at) VALUES (:first_name, :last_name, :email, :password, NOW())"
				# we'll then create a dictionary of data from the POST data received
				data = {
					'first_name' : user_info['first_name'],
					'last_name' : user_info['last_name'],
					'email' : user_info['email'],
					'password' : pw_hash
					}
				self.db.query_db(query, data)
				# Then retrieve the last inserted user.
				get_user_query = "SELECT * FROM users ORDER BY id DESC LIMIT 1"
				user = self.db.query_db(get_user_query)
				return { "status": True, "user": user[0] }

	def login_user(self, user_info):
		login_errors = []
		if not user_info['email']:
			login_errors.append('username field cannot be blank')
		if not user_info['password']:
			login_errors.append('password field cannot be blank')
		if login_errors:
			return {"status": False, "login_errors": login_errors}

		else:   
			password = user_info['password']
			query = "SELECT * FROM users WHERE email = :email LIMIT 1"
			user_data = {'email': user_info['email']}
			user = self.db.query_db(query, user_data)
			if user and self.bcrypt.check_password_hash(user[0]['password'], password):
				return { "status": True, "user": user[0] }
			else:
				login_errors.append("Invalid login. Username or password doesnt match our database")
				return {"status": False, "login_errors": login_errors}

	def get_user(self, id):
		print id
		query = "SELECT id, CONCAT(users.first_name, ' ', users.last_name) AS name, created_at FROM users where id = :id"
		data = {'id': id }
		return self.db.get_one(query, data)