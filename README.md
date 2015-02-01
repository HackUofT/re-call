# re-call
Leave your future self aggressive reminders so that you can get shit done later. An iOS app.

##use case

You've just had delicious poutine at U of T Hacks and you really need to go to the gym later. You create a reminder, record yourself saying "GO TO THE GYM YOU LAZY PERSON", and set the app to call you and play the recording on Monday, when you plan to go to the gym.

##screen shots
![alt text](https://github.com/HackUofT/re-call/blob/master/imagesForReadMe/mainscreen.jpg "Main screen")
![alt text](https://github.com/HackUofT/re-call/blob/master/imagesForReadMe/addtaskscreen.jpg "Add a reminder")
![alt text](https://github.com/HackUofT/re-call/blob/master/imagesForReadMe/addscreen.jpg "Reminder times")

##stack
Flask
Heroku
Swift iOS app

##details
Twilio number: +15873169685

##learning resources

###flask + sqlite3 database tutorial for making a microblog
http://flask.pocoo.org/docs/0.10/tutorial/schema/#tutorial-schema

###flask + heroku tutorial
https://devcenter.heroku.com/articles/getting-started-with-python-o#prerequisites

###swift photo filter tutorial
https://developer.apple.com/swift/blog/?id=16

###heroku + python tutorial
https://devcenter.heroku.com/articles/getting-started-with-python#introduction

###APScheduler + heroku tutorial
https://devcenter.heroku.com/articles/clock-processes-python

###Redis queue tutorial (for running scheduled class outside of clock.py)
https://devcenter.heroku.com/articles/python-rq


#### development notes
the flask\_heroku_sqlite3 folder contains a microblog app that allows you to input an audio file (one of "static/a.wav", "static/b.wav", ... , "static/g.wav") or text, plus a title, for a microblog post. it has all the infrastructure necessary to store data from the re-call.me app. We still have to make the Swift front end, and get Swift to save recordings into the static folder and put data entries into the database (and retreive them).

### running aishi's flask/twilio/heroku app
run the following commands:

```
> sudo pip install Flask gunicorn apscheduler twilio rq
> heroku login
> heroku create
> git push heroku master
> heroku ps:scale web=1
> heroku scale worker=1
> heroku ps:scale clock=1
> heroku open
```

go to app URL /voice to rickroll the hard-coded phone number

database is called remindme.db

to run command locally:
```
> virtualenv venv
> source venv/bin/activate
> pip install Flask gunicorn schedule twilio
> foreman start
```
app will be hosted at http://localhost:5000/
