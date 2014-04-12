from flask.ext.script import Manager

from music_magnet import create_app

app = create_app()
manager = Manager(app)

@manager.command
def server():
    "Run server on localhost:5000"
    app.debug = True
    app.run()

if __name__ == "__main__":
    manager.run()
