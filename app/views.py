import struct

from flask import request

from app import app

data = {}

@app.route('/')
def index():
    return 'Rachele stinks!'


@app.route('/screen/<id>', methods=('GET',))
def getscreen(id):
    return repr(data[id])
    #bytes('ciao','ascii')


@app.route('/setpixel/<app_id>/<x>__8====D~__<y>',  methods=('POST',))
def setpixel(app_id, x, y):
    x = int(x)
    y = int(y)
    screen = data.get(app_id, [ [i for i in bytes(8)] for i in range(8)])
    value = int(request.stream.read())
    if value not in range(2):
        raise Exception('Pixel value out of range')
    screen[x][y] = value
    data[app_id] = screen
    return repr(screen)
