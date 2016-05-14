Run this thing
==============

It requires python3 and python3-flask.

```
./run
```

Runs a test server that listens on 0.0.0.0:5000

The daemon is the item that communicates with the arduino device. It accepts a hostname and a port on the command line, which are pointing to the webserver started by the previous command.

It listens to port 12345

App interaction
===============

* Set pixel
```
POST /setpixel/<appid>/<x>__8====D~__<y>
```

<appid> is an unique identifier for the app.
<x>,<y> are inegers from 0 to 7.

The post data can be either "1" or "0"

