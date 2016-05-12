Run this thing
==============

It requires python3 and python3-flask.

```
./run
```

Runs a test server that listens on 0.0.0.0:5000

App interaction
===============

* Set screen
```
POST /setscreen/<appid>
```

<appid> is an unique identifier for the app.

The POST data is the data that the app wants to display on the screen.


