from flask import Flask, render_template
import mysql.connector
import requests
app = Flask(__name__)

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="admin",
#   passwd="secret"
# )

# print(mydb)

@app.route('/')
def hello_world():
	suma = 100+200
	return render_template('index.html', suma=suma)

@app.route('/raul')
def raul():
    return '<h1>Hola Raul!</h1> <p> que pasa raul </p>'

@app.route('/posts')
def posts():
	URL = "https://jsonplaceholder.typicode.com/posts"
	posts = requests.get(url=URL)
	posts = posts.json()

	# users available
	users = []
	for post in posts:
		user_id = post['userId']
		if not user_id in users:
			users.append(user_id)
	print(users)

	total_users = len(users)

	#
	diccionario= {}
	for user in users:
		for post in posts:
			if post['userId'] == user:
				if user in diccionario.keys():
					diccionario[user] = diccionario[user] + 1
				else:
					diccionario[user] = 1

	print(diccionario)

	return render_template('posts.html', posts=posts, total_users=total_users, diccionario=diccionario)