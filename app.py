from flask import Flask, render_template ,request
from flask_socketio import SocketIO, emit
import logging
import random


logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(data):
    encrypted_message = data['message']
    sender = data['sender']

    
    char_map = {
        'a':'10v-1',
        'b': '10',
        'c': '0',
        'd': '01',
        'e': '1111',
        'f':'111',
        'g':'00',
        'h':'100',
        'i':'1',
        'j':'001',
        'k':'1011',
        'l':'l000',
        'm':'11111',
        'n': '101',
        'o':'000',
        'p':'100',
        'q':'001',
        'r':'1001',
        's':'1010101',
        't':'10010101',
        'u': '101',
        'v':'101',
        'w':'11011',
        'x':'0100010',
        'y':'10010',
        'z':'10101',
        
        
        
    }

    
    result = ''

    
    for char in sender.lower():  
        if char in char_map:
            result += char_map[char] + ''
        else:
            result += char + ''  

    random_number = random.randint(1, 100)
    encrypted_message_show=random_number  
    user_ip = request.remote_addr
    
    logging.debug(f"Received encrypted message: {encrypted_message_show} from  ({result.strip()}) with IP {user_ip}")

    try:
        
        emit('message', {'message': encrypted_message}, broadcast=True)
    except Exception as e:
        logging.error(f"Error processing message: {e}")
        emit('error', 'Message processing failed.')

if __name__ == '__main__':
        socketio.run(app, host='0.0.0.0', port=5000, debug=True)

