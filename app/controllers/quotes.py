"""
	Sample Controller File

	A Controller should be in charge of responding to a request.
	Load models to interact with the database and load views to render them to the client.

	Create a controller using this template
"""
from system.core.controller import *
import re

class quotes(Controller):
	def __init__(self, action):
		super(quotes, self).__init__(action)
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
   
	
	def quotes(self):
		#grab quotes, grab favorites, post new quotes
		user_info = {
			"user_id" : session['id']
		}
		one_user = self.models['quote'].get_user()
		all_quotes = self.models['quote'].get_quotes()
		all_favorites = self.models['quote'].get_favorites(user_info)
		return self.load_view('wall.html', one_user=one_user, all_quotes=all_quotes, all_favorites=all_favorites)

	def post(self, id):
		user_info = {
			"user_id" : session['id'],
			"author_name" : request.form['author_name'],
			"quote" : request.form['quote'],
		}
		self.models['quote'].post(user_info, id)
		# if postmsg_status['status'] == True:
		# 	one_user = self.models['usersModel'].get_user(id)
		return redirect('/quotes')

	def add(self, id):
		quote = self.models['quote'].get_quote(id)
		user_info = {
				"user_id" : session['id'],
				"favorite" : quote[0]['quote'],
			}
		self.models['quote'].add(user_info)
