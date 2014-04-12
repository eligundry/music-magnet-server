from flask.ext.api import FlaskAPI
from tpb import TPB

tpb = TPB('https://thepiratebay.org')

def create_app(config_objects=['music_magnet.settings.site']):
    app = FlaskAPI(__name__)

    for config_object in config_objects:
        app.config.from_object(config_object)

    from music_magnet.views import search

    app.register_blueprint(search.blueprint)

    return app
