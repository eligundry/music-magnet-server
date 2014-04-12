import time

from music_magnet import tpb, lf
from music_magnet.views import *

blueprint = Blueprint('search', __name__)

@blueprint.route('/search', methods=['GET'])
#@set_renderers(JSONRenderer)
def search_last_fm():
    """
    Searches last.fm for 5 artists, 5 albums, and 5 songs
    """

    query = request.args.get('q')
    result = {
        'artists': {},
        'albums': {},
        'tracks': {},
    }

    artists = lf.search_for_artist(query).get_next_page()
    albums = lf.search_for_album(query).get_next_page()
    tracks = lf.search_for_track(query).get_next_page()

    for artist in artists:
        result['artists'].update({
            "name": artist.name,
        })

    for album in albums:
        result['albums'].update({
            "artist": album.artist.name,
            "title": album.title,
        })

    for track in tracks:
        result['tracks'].update({
            "title": track.title,
        })

    return result
