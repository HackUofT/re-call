from flask import Flask, request, redirect
import twilio.twiml
 
app = Flask(__name__)
 
 
@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    #get number from caller
    from_number = request.values.get('From', None)

    resp = twilio.twiml.Response()
    # Greet the caller by name
    resp.say("Hello ")
    # Play an mp3
    resp.play("http://demo.twilio.com/hellomonkey/monkey.mp3")
 
    # Gather digits.
    with resp.gather(action="/handle-key", method="POST") as g:
        g.say("""Record your own monkey howl.""")
 
    return str(resp)
 
@app.route("/handle-key", methods=['GET', 'POST'])
def handle_key():

    resp = twilio.twiml.Response()
    resp.say("Record your monkey howl after the tone.")
    resp.record(maxLength="30", action="/handle-recording")
    return str(resp)
 
 
@app.route("/handle-recording", methods=['GET', 'POST'])
def handle_recording():
    """Play back the caller's recording."""
 
    recording_url = request.values.get("RecordingUrl", None)
 
    resp = twilio.twiml.Response()
    resp.say("Thanks for howling... take a listen to what you howled.")
    resp.play(recording_url)
    resp.say("Goodbye.")
    return str(resp)
 
if __name__ == "__main__":
    app.run(debug=True)