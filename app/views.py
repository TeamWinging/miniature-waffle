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

@app.route('/setapp', methods=('POST',))
def setapp():
    '''
    POST
    sets the currently shown app
    '''
    screen_mapping[0] = request.stream.read()
    return 'OK'

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

@app.route('/icon/<app_id>/<icon_id>',  methods=('GET',))
def icon(app_id, icon_id):
    '''
    Sets the value for a pixel.

    app_id is the unique identifier for the app

    icon_id is the icon identifier.

    '''

    rain = [
        [0,0,1,1,1,1,0,0],
        [0,1,1,0,0,1,1,0],
        [1,0,0,0,0,0,0,1],
        [1,1,1,1,1,1,1,1],
        [0,0,0,0,1,0,0,0],
        [0,0,0,0,1,0,0,0],
        [0,0,0,0,1,0,0,0],
        [0,0,0,1,1,0,0,0]
    ]

    four = [
        [0,0,0,0,1,0,0,0],
        [0,0,0,1,0,0,0,0],
        [0,0,1,0,0,0,0,0],
        [0,1,0,0,1,0,0,0],
        [1,1,1,1,1,1,1,0],
        [0,0,0,0,1,0,0,0],
        [0,0,0,0,1,0,0,0],
        [0,0,0,0,1,0,0,0]
        ]

    three = [
        [0,0,1,1,1,0,0,0],
        [0,1,0,0,0,1,0,0],
        [0,0,0,0,0,1,0,0],
        [0,0,0,0,1,0,0,0],
        [0,0,0,0,0,1,0,0],
        [0,0,0,0,0,1,0,0],
        [0,1,0,0,0,1,0,0],
        [0,0,1,1,1,0,0,0]
        ]

    two = [
        [0,0,1,1,1,0,0,0],
        [0,1,0,0,0,1,0,0],
        [0,0,0,0,0,1,0,0],
        [0,0,0,0,0,1,0,0],
        [0,0,0,0,1,0,0,0],
        [0,0,0,1,0,0,0,0],
        [0,0,1,0,0,0,0,0],
        [0,1,1,1,1,1,0,0]
        ]

    one = [
        [0,0,0,0,1,0,0,0],
        [0,0,0,1,1,0,0,0],
        [0,0,1,0,1,0,0,0],
        [0,0,0,0,1,0,0,0],
        [0,0,0,0,1,0,0,0],
        [0,0,0,0,1,0,0,0],
        [0,0,0,0,1,0,0,0],
        [0,0,0,1,1,1,0,0]
        ]

    zero = [
        [0,0,1,1,1,1,0,0],
        [0,1,0,0,0,0,1,0],
        [0,1,1,0,0,0,1,0],
        [0,1,0,1,0,0,1,0],
        [0,1,0,0,1,0,1,0],
        [0,1,0,0,0,1,1,0],
        [0,1,0,0,0,0,1,0],
        [0,0,1,1,1,1,0,0]
        ]

    sun = [
        [1,0,0,1,0,0,1,0],
        [0,1,0,1,0,1,0,0],
        [0,0,1,1,1,0,0,0],
        [1,1,1,0,1,1,1,0],
        [0,0,1,1,1,0,0,0],
        [0,1,0,1,0,1,0,0],
        [1,0,0,1,0,0,1,0],
        [0,0,0,0,0,0,0,0]
        ]

    cloud = [
        [0,0,0,0,0,0,0,0],
        [0,1,0,0,0,0,0,0],
        [1,1,1,0,1,1,0,0],
        [0,1,0,1,1,1,1,0],
        [0,0,1,1,1,1,1,1],
        [0,1,1,1,1,1,1,1],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0]
        ]

    d = {
        'rain': rain,
        'cloud': cloud,
        'sun': sun,
        'zero': zero,
        'one': one,
        'two': two,
        'three': three,
        'four': four,
        }
    try:
        data[app_id] = d[icon_id]
    except:
        pass
    return ""


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


@app.route('/setrow/<app_id>/<x>',  methods=('POST',))
def setrow(app_id, x):
    '''
    Sets the values for a row

    app_id is the unique identifier for the app

    x is the value of the row

    Only 1 byte is allowed in the POST payload.

    It can either be '1' or '0'
    '''
    x = int(x)
    value = int(request.stream.read())
    if value not in range(2):
        raise Exception('Pixel value out of range')
    screen = getscreen(app_id)
    screen[x] = [value for i in range(8)]
    data[app_id] = screen
    return repr(screen)


@app.route('/setcol/<app_id>/<y>',  methods=('POST',))
def setcol(app_id, y):
    '''
    Sets the values for a row

    app_id is the unique identifier for the app

    y is the value of the column

    Only 1 byte is allowed in the POST payload.

    It can either be '1' or '0'
    '''
    y = int(y)
    value = int(request.stream.read())
    if value not in range(2):
        raise Exception('Pixel value out of range')
    screen = getscreen(app_id)

    for r in range(8):
        screen[r][y] = value
    data[app_id] = screen
    return repr(screen)
