import struct

from flask import request

from app import app

_validate = {'epoch': int, 'addr': str, 'username': str, 'result': bool}

@app.route('/')
def index():
    return 'Rachele stinks!'

@app.route('/screen/<id>', methods=('GET',))
def getscreen(id):
    return bytes('ciao','ascii')

