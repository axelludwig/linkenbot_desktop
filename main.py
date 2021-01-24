import socketio

from pynput.keyboard import Key, Listener
import logging

log_dir = ""

# logging.basicConfig(filename=(log_dir + "key_log.txt"),
#                     level=logging.DEBUG, format='%(asctime)s: %(message)s')

sio = socketio.Client()

sio.connect('http://194.147.2.105:8000')

list = []
def manageList(input):
    if (3 <= len(list)):
        list[0] = list[1]
        list[1] = list[2]
        list[2] = input
    else:
        list.append(input)
        if (3 != len(list)):
            return
    print(list)
    if ('Key.ctrl_l' != list[0] or 'Key.ctrl_l' == list[1] or 'Key.ctrl_l' == list[2]):
        return
    else:
        if ("<class 'str'>" == str(type(list[1])) and "<class 'str'>" == str(type(list[2]))):
            code = list[1] + list[2]
            if ('11' == code):
                sio.emit('command', {'code': '11'})
                print('sent code ' + code)
            elif ('12' == code):
                sio.emit('command', {'code': '12'})
                print('sent code ' + code)
            elif ('13' == code):
                sio.emit('command', {'code': '13'})
                print('sent code ' + code)
        else:
            print('erreur')


def formatKeys(key):
    key = str(key)
    if ('<' == key[0]):
        key = key[:-1][1:]
        key = int(key) % 96
        return str(key)
    elif('Key.ctrl_l' == key):
        return str(key)


def on_press(key):
    manageList(formatKeys(key))
    # logging.info(str(key))
    # print(format(key))
    # manageList(str(key))
    # if ('<97>' == str(key)):
    #     print('touche 1')
    #     manageList(str(key))
    #     list.append(str(key))

    #     # sio.emit('my response', {'response': 'my response'})
    #     # sio.emit('keyPress', {'key': '1'})
    # elif ('<98>' == str(key)):
    #     print('touche 2')
    #     # sio.emit('keyPress', {'key': '2'})
    #     test()


with Listener(on_press=on_press) as listener:
    listener.join()


# dans l'event keylogger zjouter a une liste, lire la liste en dehors


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


# sio.emit('keyPress', {'key': '1'})
# sio.wait()

# while 1:
#     input("Press Enter to continue...")
#     sio.emit('my response', {'response': 'my response'})
