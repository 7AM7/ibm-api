import flask
from flask import request, flash,abort
import json, os
from api import *

app = flask.Flask(__name__)

browser = None
@app.route('/', methods=['GET'])
def home():
	return '<h1> Hello to API </h1>'
	
@app.route('/open', methods=['POST'])
def open():
	global browser
	browser = create_broswer()
	if browser is None:
		return "Open filed"
	return "Open done"
	
@app.route('/registration', methods=['POST'])
def registration():
	
	content = request.get_json()
	first_name = content["first_name"]
	last_name = content['last_name']
	email = content['email']
	password = content['password']

	response = registration_post_data(browser, email, first_name, last_name, password)
	if response == "True":
		return 'Registration done'
	return response

@app.route('/verification', methods=['POST'])
def verification():
	content = request.get_json()
	digit_code = content['digit_code']
	response = verification_post_data(browser, digit_code)
	if response == 'True':
		return 'Verification done'
	return response

@app.route('/close', methods=['POST'])
def close():
	browser.delete_all_cookies()
	browser.close()
	return "Close done"
