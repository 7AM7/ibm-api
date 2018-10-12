import flask
from flask import request, flash,abort
import json
from main import *
app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['POST'])
def home():
    print (request.is_json)
    content = request.get_json()
    print (content['first_name'])
    return 'JSON posted'

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
    # browser.delete_all_cookies()
    # browser.close()
    if response == 'True':
        return 'Verification done'
    return response

if __name__ == '__main__':
    browser = create_broswer()
    app.run()
   