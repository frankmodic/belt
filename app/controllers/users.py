"""
	Sample Controller File

	A Controller should be in charge of responding to a request.
	Load models to interact with the database and load views to render them to the client.

	Create a controller using this template
"""
from system.core.controller import *

class users(Controller):
	def __init__(self, action):
		super(users, self).__init__(action)
		"""
			This is an example of loading a model.
			Every controller has access to the load_model method.
		"""
		self.load_model('user')
		self.load_model('quote')
		self.db = self._app.db

		"""
		
		This is an example of a controller method that will load a view for the client 

		"""
   
	def index(self):
		"""
		A loaded model is accessible through the models attribute 
		self.models['WelcomeModel'].get_users()
		
		self.models['WelcomeModel'].add_message()
		# messages = self.models['WelcomeModel'].grab_messages()
		# user = self.models['WelcomeModel'].get_user()
		# to pass information on to a view it's the same as it was with Flask
		
		# return self.load_view('index.html', messages=messages, user=user)
		"""
		return self.load_view('index.html')

	def create(self):
		user_info = {
			"first_name" : request.form['first_name'],
			"last_name" : request.form['last_name'],
			"email" : request.form['email'],
			"password" : request.form['password'],
			"pw_confirmation" : request.form['pw_confirmation']
		}
		
		create_status = self.models['user'].create_user(user_info)
		if create_status['status'] == True:
			if 'id' not in session:
				session['id'] = create_status['user']['id'] 
			if 'first_name' not in session:
				session['first_name'] = create_status['user']['first_name']
			# we can redirect to the users profile page here
			return redirect('/quotes')
		else:
			for message in create_status['regis_errors']:
				flash(message, 'regis_errors')
			# redirect to the method that renders the form
			return redirect('/')

	def login(self):
			user_info = {
				"email" : request.form['email'],
				"password" : request.form['password']
				}
			user = self.models['user'].login_user(user_info)
			if user['status'] == True:
				session['id'] = user['user']['id'] 
				session['first_name'] = user['user']['first_name']
				return redirect('/quotes')
			# check_password_hash() compares encrypted password in DB to one provided by user logging in
			
			# Whether we did not find the email, or if the password did not match, either way return False
			else:
				if user['status'] == False:
					for message in user['login_errors']:
						flash(message, 'login_errors')
					# redirect to the method that renders the form
					return redirect('/')


	def show(self, id):
		user_info = {
			"user_id" : session['id']
		}
		one_user = self.models['user'].get_user(id)
		quotes = self.models['quote'].get_quote(id)
		return self.load_view('show.html', one_user=one_user, quotes=quotes)

	def logout(self):
		session.clear()
		return redirect('/')

