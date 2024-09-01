import socketio
import re
from dotenv import load_dotenv, set_key  # Required to manage .env file easily
import os 
import listener
import json

load_dotenv('.env')
app = listener.FileViewer()

# Socket token from /socket/token endpoint
socket_token = os.environ['SOCKET_TOKEN']
commands = {}
# Create a Socket.IO client
sio = socketio.Client(logger=True, engineio_logger=True)

# Connect event
@sio.event
def connect():
    print("Connected to Streamlabs")
import random
# Event handler for different types of messages
@sio.on('event')
def on_message(data):
    global commands
    if not commands:
        commands = read_json_file("commands.json")
    speaker = ""
    found = False
    if data['type'] == 'alertPlaying':
        if 'message' in data and 'message' in data['message']:
            if "|" in data['message']['message'].lower():
                speaker = data['message']['message'].split("|")[1].lower().strip() 
                speaker = commands[speaker]
                found = True
                print(f'\n\nspeaker: {speaker}')
            elif "test donation" in data['message']['message'].lower():
                print('Test Donation Speaker Test')
                length = len(commands)
                random_index = random.randint(0, length - 1)
                x = 0
                for i, v in commands.items():
                    if x == random_index:
                        speaker = v
                        print(f'\n\n{speaker}')
                        found = True
                        break
                    x += 1
                print(f'\n\n{speaker}')
                found = True
            else:
                print('No speaker found')
            if found:
                try:
                    with open('config.txt', 'w') as f:
                        f.write(json.dumps(speaker))
                except Exception as e:
                    print(str(e))
                
def speakerchange(speaker):
    with open('speaker.txt', 'w') as f:
        f.write(speaker)


def read_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data


# Disconnect event
@sio.event
def disconnect():
    print("Disconnected from server")

# Connect to Streamlabs using the token
sio.connect(f'https://sockets.streamlabs.com?token={socket_token}', transports='websocket')

# Wait for events
try:
    sio.wait()
except KeyboardInterrupt:
    sio.disconnect()
