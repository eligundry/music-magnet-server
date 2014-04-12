from flask.ext.script import Manager

from music_magnet import create_app


app = create_app()
manager = Manager(app)

def server():
    "Run server on localhost:5000"
    app.debug = True
    app.run()
