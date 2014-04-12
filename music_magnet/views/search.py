import time

from music_magnet import lf, discogs
from music_magnet.views import *

blueprint = Blueprint('search', __name__)

@blueprint.route('/search', methods=['GET'])
def search_tpb():
    """
    Searches The Pirate Bay for music
    """

    query = request.args.get('q')

    result = []

    return result
