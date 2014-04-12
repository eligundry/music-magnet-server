from flask.ext.api import FlaskAPI
import pylast
import discogs_client as discogs

lf = pylast.LastFMNetwork()

def create_app(config_objects=['music_magnet.settings.site']):
    app = FlaskAPI(__name__)

    for config_object in config_objects:
        app.config.from_object(config_object)

    # Configure last.fm connection
    lf.api_key = app.config['LAST_FM_PUBLIC_KEY']
    lf.api_secret = app.config['LAST_FM_SECRET_KEY']

    # Configure discogs user agent
    discogs.user_agent = 'MusicMagnet/0.1 +http://music-magnet.eligundry.com'

    from music_magnet.views import search

    app.register_blueprint(search.blueprint)

    return app
