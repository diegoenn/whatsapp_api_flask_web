import json
from flask import Flask, render_template, request
from message_helper import get_templated_message_input, get_text_message_input, send_message
import flask
from flights import get_flights
 
app = Flask(__name__)
 
with open('config.json') as f:
    config = json.load(f)
 
app.config.update(config)
 
@app.route("/")
def index():
    return render_template('index.html', name=__name__)
 
@app.route('/welcome', methods=['POST'])
async def welcome():
  data = get_text_message_input(app.config['RECIPIENT_WAID']
                                , 'Welcome to the Flight Confirmation Demo Diego App for Python!');
  await send_message(data)
  return flask.redirect(flask.url_for('catalog'))
 
@app.route("/catalog")
def catalog():
    return render_template('catalog.html', title='Flight Confirmation Demo for Python', flights=get_flights())

@app.route("/buy-ticket", methods=['POST'])
async def buy_ticket():
  flight_id = int(request.form.get("id"))
  flights = get_flights()
  flight = next(filter(lambda f: f['flight_id'] == flight_id, flights), None)
  data = get_templated_message_input(app.config['RECIPIENT_WAID'], flight)
  await send_message(data)
  return flask.redirect(flask.url_for('catalog'))