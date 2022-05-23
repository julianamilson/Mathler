from flask import Flask, request, render_template, Response
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
		request_body_JSON = request.get_json()
	response_body = JSON_wrap(mathler.mathler(request_body_JSON['guess']))
	response_body_JSON = json.loads(response_body)
	return response_body_JSON

@app.route('/favicon.ico')
def favicon():
	return ""

@app.route('/README.md')
def readMe():
	return ("README.md")

def JSON_wrap(msg):
	msg_JSON = "{\""
	if len(msg) == 6:
		msg_JSON += "clue\":\""
	else:
		msg_JSON += "error\":\""
	msg_JSON += msg
	msg_JSON += "\"}"
	return msg_JSON


if __name__== "__main__":
	app.run(debug=True)
