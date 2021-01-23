import socketio

from pynput.keyboard import Key, Listener
import logging

log_dir = ""

# logging.basicConfig(filename=(log_dir + "key_log.txt"),
#                     level=logging.DEBUG, format='%(asctime)s: %(message)s')


def on_press(key):
    # logging.info(str(key))
    print(str(key))


# with Listener(on_press=on_press) as listener:
#     listener.join()

sio = socketio.Client()


@sio.event
def connect():
    print('connection established')


@sio.event
def my_message(data):
    print('message received with ', data)
    sio.emit('my response', {'response': 'my response'})


@sio.event
def disconnect():
    print('disconnected from server')


sio.connect('http://localhost:8001')
# sio.wait()

while 1:
    input("Press Enter to continue...")
    sio.emit('my response', {'response': 'my response'})
