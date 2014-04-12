from flask import Flask
from tpb import TPB
import pylast

tpb = TPB('https://thepiratebay.org')
lf = pylast.LastFMNetwork()

def create_app(config_objects=['music_magnet.settings.site']):
    app = Flask(__name__)

    for config_object in config_objects:
        app.config.from_object(config_object)

    lf.api_key = app.config['LAST_FM_PUBLIC_KEY ']
    lf.api_secret = app.config['LAST_FM_SECRET_KEY ']

    return app
