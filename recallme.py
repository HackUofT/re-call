# all the imports
import os
import sqlite3
import clock
import jsonify
import twilio.twiml
from twilio.rest import TwilioRestClient
from flask import Flask, request, session, g, redirect, url_for, \
abort, render_template, flash
from contextlib import closing

# configuration
DATABASE = '/tmp/flaskr.db'
DEBUG = True
SECRET_KEY = 'development key'
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

init_db()

@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()

@app.route("/", methods=['GET', 'POST'])
def show_entries():
    """Respond to incoming calls with a simple text message."""

    #get number from caller
    from_number = request.values.get('From', None)

    resp = twilio.twiml.Response()
    resp.message("Go to the fucking gymmmmmmmm")
    resp.say("Record your message to yourself after the tone.")
    resp.record(maxLength="15", action="/handle-recording")

    # show_entries from http://flask.pocoo.org/docs/0.10/tutorial/views/#tutorial-views
    cur = g.db.execute('select title, text from entries order by id desc')
    entries = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]
    return render_template('show_entries.html', entries=entries)


@app.route('/add', methods=['POST'])
def add_entry():




    # line below needs to be edited to put json into database from post request
    g.db.execute('insert into entries (title, audioFile, text, eventTime, eventDate, reminderTime, reminderDate) values (?, ?, ?, ?, ?, ?, ?)',
                 [request.form['title'], request.form['audioFile'], request.form['text'], request.form['eventTime'], request.form['eventDate'], request.form['reminderTime'], request.form['reminderDate']])

    #NEED TO SCHEDULE REMINDER
    #new_reminder(request.form['reminderDate'])
    voice_reminder()

    g.db.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))


 
@app.route("/voice", methods=['GET', 'POST'])
def voice_reminder():
    call = client.calls.create(url="http://demo.twilio.com/docs/voice.xml",
        to="+16478683107", 
        from_="+15873169685")
    print call.sid 
    return(call.sid)
 
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
 


