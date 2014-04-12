from music_magnet import tpb
from music_magnet.views import *

blueprint = Blueprint('search', __name__)

@blueprint.route('/search')
def search_last_fm():
    """
    Searches last.fm
    """
    return {}
