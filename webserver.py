from flask import Flask, request, render_template
import mathler
import json

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
	content_type = request.headers.get('Content-Type')
	if (content_type == 'application/json'):
		print("content type ok !!")
		k = request.get_json()
		print("get!!")
		print(k)
		print(k['guess'])
		print(type(k['guess']))
		#print(obj['guess'])
	else:
		print("wrong content type")
		print(content_type)
		print(request)
	return mathler.mathler(k['guess'])
	# print("teste")
	# y = request.json
	# print("teste2")
	# print(y)
	# print("teste3")
	# return mathler.getClue("40+1+1", request.data)

@app.route('/teste')
def testingEndpoint():
	return mathler.getClue("40+1+1", "40+1+1")

@app.route('/README.md')
def readMe():
	return ("README.md")
# @app.route('/clue', methods=['POST'])
# def testgoGetClue():
# 	data = request.args.get ('guess')
# 	return mathler.mathler(data)

if __name__== "__main__":
	app.run(debug=True)
