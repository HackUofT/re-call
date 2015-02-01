# re-call
Leave your future self aggressive reminders so that you can get shit done later. An iOS app.

##use case

You've just had delicious poutine at U of T Hacks and you really need to go to the gym later. You create a reminder, record yourself saying "GO TO THE GYM YOU LAZY PERSON", and set the app to call you and play the recording on Monday, when you plan to go to the gym.

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


#### development notes
the flask\_heroku_sqlite3 folder contains a microblog app that allows you to input an audio file (one of "static/a.wav", "static/b.wav", ... , "static/g.wav") or text, plus a title, for a microblog post. it has all the infrastructure necessary to store data from the re-call.me app. We still have to make the Swift front end, and get Swift to save recordings into the static folder and put data entries into the database (and retreive them).
