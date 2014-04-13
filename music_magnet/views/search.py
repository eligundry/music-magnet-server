import time
import kat

from tpb import TPB, CATEGORIES, ORDERS

from music_magnet import lf
from music_magnet.views import *

blueprint = Blueprint('search', __name__)
tpb = TPB('https://thepiratebay.org')

@blueprint.route('/search/kat', methods=['GET'])
def search_kat():
    """
    Searches Kickass Torrents for torrent info
    """

    result = []
    query = request.args.get('q')
    torrents = kat.search(query, category=kat.Categories.MUSIC,
            sort=kat.Sorting.SEED, order=kat.Sorting.Order.DESC)

    for torrent in torrents:
        result.append({
            'title': torrent.title,
            'magnet': torrent.magnet,
        })

    return result

@blueprint.route('/search/tpb', methods=['GET'])
def search_tpb():
    """
    Searches The Pirate Bay for torrent info
    """

    result = []
    query = request.args.get('q')
    torrents = tpb.search(query, category=CATEGORIES.AUDIO,
            order=ORDERS.SEEDERS.DES)

    for torrent in torrents.items():
        if torrent.sub_category != CATEGORIES.AUDIO.FLAC:
            result.append({
                'title': torrent.title,
                'magnet': torrent.magnet_link,
                'file_list': sorted(torrent.files),
            })

    return result


@blueprint.route('/search/lastfm/artist', methods=['GET'])
def search_last_fm():
    """
    Searches Last.fm for artists
    """
    result = []

    return result
