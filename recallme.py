# all the imports
import os
import sqlite3
import twilio.twiml
from twilio.rest import TwilioRestClient
from flask import Flask, request, session, g, redirect, url_for, \
abort, render_template, flash
from contextlib import closing

app = Flask(__name__)

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC23e9837805043e0ab73db0164f2ae9e1"
auth_token  = "0e8bdf4642daf804bbd5c2c5bf36b4be"
client = TwilioRestClient(account_sid, auth_token)

def connect_db():
	return sqlite3.connect(app.config['DATABASE'])

def init_db():
	with closing(connect_db()) as db:
		with app.open_resource('schema.sql', mode='r') as f:
			db.cursor().executescript(f.read())
	db.commit()

@app.route("/", methods=['GET', 'POST'])
def text_reminder():
    """Respond to incoming calls with a simple text message."""
 
    resp = twilio.twiml.Response()
    resp.message("Go to the fucking gymmmmmmmm")
    return str(resp)
 
@app.route("/voice", methods=['GET', 'POST'])
def voice_reminder():
	call = client.calls.create(url="http://demo.twilio.com/docs/voice.xml",
    	to="+12269841394",
    	from_="+15873169685")
	print call.sid

if __name__ == '__main__':
	app.run(debug=True)
 
 # Download the Python helper library from twilio.com/docs/python/install

 