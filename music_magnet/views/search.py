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

    args = request.args
    result = []

    if args.has_key('q') is not True:
        result = {
            'code': 400,
            'message': "You did not include a 'q' attribute to make a query with."
        }

        return result, status.HTTP_400_BAD_REQUEST

    torrents = None

    if args.has_key('page'):
        torrents = tpb.search(args['q'], page=args['page'],
                order=ORDERS.SEEDERS.DES, category=CATEGORIES.AUDIO)
    else:
        torrents = tpb.search(args['q'], order=ORDERS.SEEDERS.DES,
                category=CATEGORIES.AUDIO)


    for torrent in torrents.items():
        if torrent.sub_category != 'FLAC' and torrent.seeders != 0:
            item = {
                'id': torrent.id,
                'title': torrent.title,
                'seeders': torrent.seeders,
                'leachers': torrent.leechers,
                'magnet': torrent.magnet_link
            }

            result.append(item)

    return result

@blueprint.route('/search/tpb/<id>', methods=['GET'])
def get_tpb_torrent():
    pass

@blueprint.route('/search/lastfm/artist', methods=['GET'])
def search_last_fm():
    """
    Searches Last.fm for artists
    """
    result = []

    return result
