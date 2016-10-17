import logging
import wikipedia

from flask import Flask
from flask_ask import Ask, statement, question, session

app = Flask(__name__)
ask = Ask(app,"/")

logging.getLogger("flask_ask").setLevel(logging.DEBUG);

@ask.launch
def launch():
    welcome = 'Want to know who my favorite actor is?'
    return question(welcome)

@ask.intent('YesIntent')
def get_nick_cage():
    info = get_json_wikipedia()
    if not info:
        error = "There seems to be a problem connecting to wikipedia"
        return statement(error)
    else:
        return statement(info)

@ask.intent('AMAZON.StopIntent')
def stop():
    return statement("Goodbye")


@ask.intent('AMAZON.CancelIntent')
def cancel():
    return statement("Goodbye")

@ask.session_ended
def session_ended():
    return "", 200

def get_json_wikipedia():
    cage = wikipedia.page("Nicolas Cage")
    cage_content = 'Total bad ass Nick Cage ' + cage.content[:251] + ' ' + 'Also I like to add that David Ashe is a huge fan boy'
    return cage_content

if __name__ == '__main__':
    app.run(debug=True)
