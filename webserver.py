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

@app.route('/clues', methods=['POST'])
def goGetClue():
	print("request data:")
	print(request.data)
	print("request stripped:")
	print(request.data.strip("b"))
	return mathler.getClue("40+1+1", request.data)


@app.route('/clue', methods=['POST'])
def testgoGetClue():
	data = request.args.get ('guess')
	return mathler.mathler(data)
	

if __name__== "__main__":
	app.run()
