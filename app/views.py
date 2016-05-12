import struct

from flask import request

from app import app

data = {}

@app.route('/')
def index():
    return 'Rachele stinks!'

@app.route('/screen/<id>', methods=('GET',))
def getscreen(id):
    return data[id]
    #bytes('ciao','ascii')

@app.route('/setscreen/<app_id>', methods=('POST',))
def ciao(app_id):
    data[app_id] = request.stream.read()
    return "ok"
