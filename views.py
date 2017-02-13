from flask import render_template, redirect, url_for, request, session, flash
from ivr_phone_tree_python import app
import twilio.twiml
from ivr_phone_tree_python.view_helpers import twiml


@app.route('/')
@app.route('/ivr')
def home():
    return render_template('index.html')


@app.route('/ivr/welcome', methods=['POST'])
def welcome():
    response = twilio.twiml.Response()
    with response.gather(numDigits=1, action=url_for('menu'), method="POST") as g:
        g.play(url="https://clyp.it/tqzbajc1.mp3", loop=3)
    return twiml(response)


@app.route('/ivr/menu', methods=['POST'])
def menu():
    selected_option = request.form['Digits']
    option_actions = {'1': _english,
                      '2': _hindi}

    if option_actions.has_key(selected_option):
        response = twilio.twiml.Response()
        option_actions[selected_option](response)
        return twiml(response)

    return _redirect_welcome()

# @app.route('/ivr/planets', methods=['POST'])
# def planets():
#     selected_option = request.form['Digits']
#     option_actions = {'2': "+12024173378",
#                       '3': "+12027336386",
#                       "4": "+12027336637"}

#     if option_actions.has_key(selected_option):
#         response = twilio.twiml.Response()
#         response.dial(option_actions[selected_option])
#         return twiml(response)

#     return _redirect_welcome()


# private methods

def _english(response):
    with response.gather(numDigits=1, action=url_for('menu1'), method="POST") as g:
        g.play(url="https://clyp.it/l1qdanvq.mp3", loop=3)
    response.hangup()
    return response

    


def _hindi(response):
    with response.gather(numDigits=1, action=url_for('menu1'), method="POST") as g:
        g.play(url="https://clyp.it/l1qdanvq.mp3", loop=3)
    return response


@app.route('/ivr/menu1', methods=['POST'])

def menu1():

    selected_option = request.form['Digits']
    option_actions = {'1': _bankbalance,
                      '2': _govtschemes,
                      '3': _bcredirect}

    if option_actions.has_key(selected_option):
        response = twilio.twiml.Response()
        option_actions[selected_option](response)
        return twiml(response)

    return _redirect_welcome()


def _bankbalance(response):
    with response.gather(numDigits=1, action=url_for('menu2'), method="POST") as g:
        g.play(url="https://clyp.it/lqkcqdme.mp3", loop=3)

    return response

@app.route('/ivr/menu2', methods=['POST'])

def menu2():

    selected_option = request.form['Digits']
    option_actions =  {'1': _listenagain,
                       '5': _previousmenu}

    if option_actions.has_key(selected_option):
        response = twilio.twiml.Response()
        option_actions[selected_option](response)
        return twiml(response)

    return _redirect_welcome()

def _listenagain(response):
    with response.gather(numDigits=1, action=url_for('menu2'), method="POST") as g:
        g.play(url="https://clyp.it/lqkcqdme.mp3", loop=3)

    return response

def _previousmenu(response):
    with response.gather(numDigits=1, action=url_for('menu1'), method="POST") as g:
        g.play(url="https://clyp.it/l1qdanvq.mp3", loop=3)
    return response


def _govtschemes(response):
    with response.gather(numDigits=1, action=url_for('menu3'), method="POST") as g:
        g.play(url="https://clyp.it/2qosmazj.mp3", loop=3)

    return response

@app.route('/ivr/menu3', methods=['POST'])

def menu3():

    selected_option = request.form['Digits']
    option_actions = {'1': _apy,
                      '2': _lpg}

    if option_actions.has_key(selected_option):
        response = twilio.twiml.Response()
        option_actions[selected_option](response)
        return twiml(response)

    return _redirect_welcome()

def _apy(response):
    with response.gather(numDigits=1, action=url_for('menu4'), method="POST") as g:
        g.play(url="https://clyp.it/i3j1pq3o.mp3", loop=3)

    return response

@app.route('/ivr/menu4', methods=['POST'])
def menu4():

    selected_option = request.form['Digits']
    option_actions =  {'1': _listenscheme,
                       '5': _mainmenu}

    if option_actions.has_key(selected_option):
        response = twilio.twiml.Response()
        option_actions[selected_option](response)
        return twiml(response)

    return _redirect_welcome()

def _listenscheme(response):
    with response.gather(numDigits=1, action=url_for('menu4'), method="POST") as g:
        g.play(url="https://clyp.it/i3j1pq3o.mp3", loop=3)

    return response

def _mainmenu(response):
    with response.gather(numDigits=1, action=url_for('menu1'), method="POST") as g:
        g.play(url="https://clyp.it/l1qdanvq.mp3", loop=3)
    return response

def _lpg(response):
    with response.gather(numDigits=1, action=url_for('menu4'), method="POST") as g:
        g.play(url="https://clyp.it/i3j1pq3o.mp3", loop=3)

    return response

def _bcredirect(response):
    with response.gather(numDigits=1, action=url_for('handle'), method="POST") as g:
        g.play(url="https://clyp.it/u3z5chwa.mp3", loop=3)
    return response

@app.route('/ivr/handle', methods=['GET', 'POST'])
def handle():
    """Handle key press from a user."""

    # Get the digit pressed by the user
    digit_pressed = request.values.get('Digits', None)
    if digit_pressed == "1":
        resp = twilio.twiml.Response()
        # Dial (310) 555-1212 - connect that number to the incoming caller.
        resp.dial("+919205292715")
        # If the dial fails:
        resp.say("The call failed, or the remote party hung up. Goodbye.")

        return str(resp)

    # If the caller pressed anything but 1, redirect them to the homepage.
    else:
        return redirect("/")




def _redirect_welcome():
    response = twilio.twiml.Response()
    response.say("Returning to the main menu", voice="alice", language="en-GB")
    response.redirect(url_for('welcome'))

    return twiml(response)
