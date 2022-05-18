from flask import Flask, request, render_template
import mathler

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		return "Hello world!"
	if request.method == 'GET':
		return "World Hello!"

@app.route('/home')
def display_home():
	return (render_template('batata.html'))

@app.route('/clues')
def goGetClue():
	return mathler.getClue("40+1+1", "-42+84")

if __name__== "__main__":
	app.run(debug=True)
