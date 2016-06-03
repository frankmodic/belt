""" 
	Sample Model File

	A Model should be in charge of communicating with the Database. 
	Define specific model method that query the database for information.
	Then call upon these model method in your controller.

	Create a model using this template.
"""
from system.core.model import Model
from time import strftime

class quote(Model):
	def __init__(self):
		super(quote, self).__init__()

	def get_quotes(self):
		fetch_quotes = "SELECT quotes.id, quote, author_name from quotes ORDER BY created_at DESC"
		# data = {
		# 	'id': id,
		# }
		return self.db.query_db(fetch_quotes)

	def get_quote(self, id):
		fetch_quote = "SELECT users.id, quotes.author_name, quote, quotes.created_at, quotes.user_id FROM users JOIN quotes ON users.id = quotes.user_id WHERE user_id = :id"
		data = { 
			'id': id,
		}
		return self.db.query_db(fetch_quote, data)


	def post(self, user_info, id):
		time = strftime('%B %d, %Y, %T')
		post_errors = []
		# if not user_info['message']:
		# 	post_errors.append('Message field cannot be blank!')
		# if post_errors:
		# 	return {"status": False, "post_errors": post_errors }
		# else:
		quote_query = "INSERT INTO quotes (user_id, quote, author_name, created_at) VALUES (:user_id, :quote, :author_name, NOW())"
		data ={
			'user_id': user_info['user_id'],
			'quote': user_info['quote'],
			'author_name': user_info['author_name'],
			'created_at': time
		}
		return self.db.query_db(quote_query, data)
		return true

	def get_user(self):
		print id
		query = "SELECT id, CONCAT(users.first_name, ' ', users.last_name) AS name, created_at FROM users where id = :id"
		data = {'id': id }
		return self.db.get_one(query, data)

	def add(self, user_info):
		time = strftime('%B %d, %Y, %T')
		add_favorite = "INSERT INTO favorites (user_id, favorite, created_at) VALUES (:user_id, :favorite, NOW()) WHERE quote_id = :favorites.quote_id"
		data = {
				"user_id" : user_info['user_id'],
				"favorite" : user_info['favorite'],
				'created_at': time
		}
		return self.db.query_db(add_favorite, data)
		return true

	def get_favorites(self, user_info):
		get = "SELECT * FROM favorites WHERE favorites.user_id = :user_id"
		data = {
			"user_id" : user_info['user_id'],
		}
		return self.db.query_db(get, data)

		