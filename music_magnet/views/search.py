import time
import kat
import re

from tpb import TPB, CATEGORIES, ORDERS

from music_magnet import lf
from music_magnet.views import *

blueprint = Blueprint('search', __name__)
tpb = TPB('https://thepiratebay.org')
year_match = re.compile('[0-9]{4}')

@blueprint.route('/kat', methods=['GET'])
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

@blueprint.route('/tpb', methods=['GET'])
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

@blueprint.route('/lastfm', methods=['GET'])
def search_last_fm():
    """
    Searches Last.fm for artists
    """
    args = request.args
    result = []

    if args.has_key('q') is not True:
        result = {
            'code': 400,
            'message': "You did not include a 'q' attribute to make a query with."
        }

        return result, status.HTTP_400_BAD_REQUEST

    artists = lf.search_for_artist(args['q']).get_next_page()

    for artist in artists[0:6]:
        item = {
            'name': artist.name,
            'image': artist.get_cover_image(size=2),
        }

        result.append(item)

    return result

@blueprint.route('/lastfm/<artist>', methods=['GET'])
def get_artist(artist):
    """
    Gets a single artist from Last.fm
    """
    artist = lf.get_artist(artist)
    result = {
        'name': artist.name,
        'cover_image': artist.get_cover_image(size=2),
        'bio_summary': artist.get_bio_summary(),
        'albums': [],
    }

    for album in artist.get_top_albums():
        year = re.search(year_match, album.item.get_release_date())

        item = {
            'title': album.item.title,
            'image': album.item.get_cover_image(size=2),
            'year': year.group(0) if year is not None else None,
        }

        result['albums'].append(item)

    return result

@blueprint.route('/lastfm/<artist>/<album>', methods=['GET'])
def get_album(artist, album):
    alb = lf.get_album(artist, album)
    year = re.search(year_match, alb.get_release_date())

    result = {
        'artist': artist,
        'title': album,
        'year': year.group(0) if year is not None else None,
        'image': alb.get_cover_image(size=2),
        'tracks': [],
    }

    for idx, track in enumerate(alb.get_tracks()):
        result['tracks'].append({
            'number': idx+1,
            'title': track.title,
        })


    return result
