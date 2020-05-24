from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
	suma = 100+200
	return render_template('index.html', suma=suma)

@app.route('/raul')
def raul():
    return '<h1>Hola Raul!</h1> <p> que pasa raul </p>'
