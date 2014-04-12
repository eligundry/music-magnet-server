import time
import kat

from music_magnet.views import *

blueprint = Blueprint('search', __name__)

@blueprint.route('/search', methods=['GET'])
def search_kat():
    """
    Searches The Pirate Bay for music
    """

    result = []
    query = request.args.get('q')
    torrents = kat.search(query, category=kat.Categories.MUSIC,
            sort=kat.Sorting.SEED, order=kat.Sorting.Order.DESC)

    for torrent in torrents:
        result.append({
            'title': torrent.title,
            'magnet': torrent._magnet,
        })

    return result
