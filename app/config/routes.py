"""
	Routes Configuration File

	Put Routing rules here
"""
from system.core.router import routes

routes['default_controller'] = 'users'
routes['GET']['/main'] = 'users#main'
routes['GET']['/users/<id>'] = 'users#show'
routes['POST']['/create'] = 'users#create'
routes['POST']['/add'] = 'users#add'
routes['POST']['/login'] = 'users#login'
routes['GET']['/logout'] = 'users#logout'
#make quotes controller/model?
routes['GET']['/quotes'] = 'quotes#quotes'
routes['POST']['/quotes/<id>'] = 'quotes#post'
routes['POST']['/add/<id>'] = 'quotes#add'

