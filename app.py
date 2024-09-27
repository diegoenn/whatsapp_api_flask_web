import json
from flask import Flask, render_template, request
from message_helper import get_templated_message_input, get_text_message_input, send_message
import flask
from flights import get_flights
 
app = Flask(__name__)

# se carga la configuracion global del archivo json en la aplicacion
with open('config.json') as f:
    config = json.load(f)
 
app.config.update(config)

# se enruta y renderiza la pagina de login inicial 
@app.route("/")
def index():
    return render_template('index.html', name=__name__)

# despues de hacer click en login se redirecciona desde welcome hacia la pagina de catalog y se envia mensaje inicial whatsapp
@app.route('/welcome', methods=['POST'])
async def welcome():
  data = get_text_message_input(app.config['RECIPIENT_WAID']
                                , 'Mensaje inicial al hacer clic en login!!!');
  print(data)
  print("login 1")
  await send_message(data)
  print("login 2")
  return flask.redirect(flask.url_for('catalog'))

# se renderiza la pagina de catalog 
@app.route("/catalog")
def catalog():
    return render_template('catalog.html', title='Flight Confirmation Demo for Python', flights=get_flights())

# despues de hacer click en buy ticket se envia mensaje de whatsapp con la informacion detallada del vuelo usando mensaje tipo template
@app.route("/buy-ticket", methods=['POST'])
async def buy_ticket():
  flight_id = int(request.form.get("id"))
  flights = get_flights()
  flight = next(filter(lambda f: f['flight_id'] == flight_id, flights), None)
  print("buy ticket 1")
  print(flight)
  print(flight['document'])
  print(flight['origin'])
  print(flight['destination'])
  print(flight['time'])
  data = get_templated_message_input(app.config['RECIPIENT_WAID'], flight)
  print("buy ticket 2")
  print(data)
  print("buy ticket 3")
  await send_message(data)
  print("buy ticket 4")
  return flask.redirect(flask.url_for('catalog'))