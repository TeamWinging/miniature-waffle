import struct

from flask import request

from app import app
from app.array2bin import convert

data = {}
screen_mapping = {}

@app.route('/')
def index():
    return 'Rachele stinks!'


def getscreen(app_id):
    '''
    Gets the screen for the app_id

    if there is no screen, returns a blank one
    '''
    return data.get(app_id, [ [i for i in bytes(8)] for i in range(8)])
    return repr(data[id])


@app.route('/listapps', methods=('GET',))
def listapps():
    '''
    Comma separated list of the available apps
    '''
    return ','.join(data.keys())


@app.route('/screencount', methods=('GET',))
def screencount():
    '''
    Returns the amount of screens
    '''
    return '%d' % len(screen_mapping)


@app.route('/screendump/<screen_id>', methods=('GET',))
def screendump(screen_id):
    '''
    Returns 64 bit of data, representing the pixels
    to set for the screen with the id
    '''
    screen_id = int(screen_id)
    app_id = screen_mapping.get(screen_id)

    if not app_id:
        # No mapping, getting a random thing
        if data:
            key = next(iter(data.keys()))
            screen = data[key]
        else:
            screen = [[i for i in bytes(8)] for i in range(8)]

    return convert(screen)


@app.route('/setpixel/<app_id>/<x>__8====D~__<y>',  methods=('POST',))
def setpixel(app_id, x, y):
    '''
    Sets the value for a pixel.

    app_id is the unique identifier for the app

    x and y are the values.

    Only 1 byte is allowed in the POST payload.

    It can either be '1' or '0'
    '''
    x = int(x)
    y = int(y)
    value = int(request.stream.read())
    if value not in range(2):
        raise Exception('Pixel value out of range')
    screen = getscreen(app_id)
    screen[x][y] = value
    data[app_id] = screen
    return repr(screen)
