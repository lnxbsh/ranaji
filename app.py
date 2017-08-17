from flask import Flask
from flask_socketio import SocketIO, send, emit
import apiai, json


#flask-socket code
app = Flask(__name__)
app.config['SECERT_KEY'] = 'key'
socketio = SocketIO(app)

#message received on new browser connection
@socketio.on('new_connection')
def handleConnection():
	send('Welcome Siddharth! You\'ve reached The Ranaji. How can Ranaji help you?')	
	print 'new connection'
	
#message sender to browser
@socketio.on('message')
def handleMessage(msg):
	msg = parse(msg)
	print msg
	send(msg)

#token for ranaji agent
CLIENT_ACCESS_TOKEN = '587197630d9446ff972459feb1364268'
 
ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)

def parse(user_text):
	request = ai.text_request()
	request.query = user_text
	response = json.loads(request.getresponse().read().decode('utf-8'))
	#print response to console
	print response
	#sending response result returned form api.ai
	return response['result']['fulfillment']['speech']

#running socketio
socketio.run(app,port=1024)
