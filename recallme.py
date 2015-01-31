# all the imports
import os
import sqlite3
import twilio.twiml
from twilio.rest import TwilioRestClient
from flask import Flask, request, session, g, redirect, url_for, \
abort, render_template, flash
from contextlib import closing

DATABASE = 'tmp/recallme.db'
DEBUG = True
SECRET_KEY = 'development_key'
USERNAME = 'admin'
PASSWORD = 'default'

app = Flask(__name__)
app.config.from_object(__name__)

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

@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()

@app.route("/", methods=['GET', 'POST'])
def text_reminder():
    """Respond to incoming calls with a simple text message."""

    #get number from caller
    from_number = request.values.get('From', None)

    resp = twilio.twiml.Response()
    resp.message("Go to the fucking gymmmmmmmm")
    resp.say("Record your message to yourself after the tone.")
    resp.record(maxLength="15", action="/handle-recording")
    return str(resp)

@app.route('/tasks', methods=['POST', 'GET'])
def show_entries():
    cur = g.db.execute('select title, text from entries order by id desc')
    entries = [dict(event_title=row[0], event_time=row[1], event_reminder_time=row[2], event_reminder_num=row[3]) for row in cur.fetchall()]
    return render_template('show_entries.html', entries=entries)
 
@app.route("/voice", methods=['GET', 'POST'])
def voice_reminder():
    call = client.calls.create(url="http://demo.twilio.com/docs/voice.xml",
        to="+12269841394",
        from_="+15873169685")
    print call.sid 
 
@app.route("/handle-recording", methods=['GET', 'POST'])
def handle_recording():
    """Play back the caller's recording."""
 
    recording_url = request.values.get("RecordingUrl", None)
 
    resp = twilio.twiml.Response()
    resp.say("Thanks for howling... take a listen to what you howled.")
    resp.play(recording_url)
    resp.say("Goodbye.")
    return str(resp)

if __name__ == '__main__':
    app.run(debug=True)
 