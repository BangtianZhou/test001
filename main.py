#created by bangtian on 20180106

from flask import jsonify
from flask import Flask, render_template, request, redirect, url_for, flash, current_app

import flask_login
import json
import os

import config
from config import *

app = Flask(__name__)

# Create flask login manager
app.secret_key = 'testing_secret_key'
login_manager = flask_login.LoginManager()
login_manager.init_app(app)

# Connect to Google Cloud SQL
#app.config.from_object(config)
#TO DO
#
#
#
#
#

# Connect to dynamoDB
db = connect_to_dynamodb()
storage = connect_to_s3()

bucket = storage.get_bucket('smileyphototest')
test_key = bucket.get_key('thumbnail_IMG_3956.jpg')
test_url = test_key.generate_url(0, query_auth=False, force_http=True)
plans_key = bucket.get_key('thumbnail_IMG_3956.jpg')
plans_url = plans_key.generate_url(3600, query_auth=True, force_http=True)
print plans_url
print test_url



"""
#  ________________________________________
# |Definition of the Login Class           |
# |________________________________________|
"""

class Login(flask_login.UserMixin):
    
    def __init__(self):
        self.exp_id = ''
        self.experience = 0
# pass

@login_manager.user_loader
def user_loader(email):
    user = Login()
    user.id = email
    return user

# Routing from here
@app.route('/', methods=['GET', 'POST'])
def test():
    return jsonify({'one':1, 'two':2})
