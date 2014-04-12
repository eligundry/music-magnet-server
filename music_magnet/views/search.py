from flask import Blueprint

search = Blueprint('search', __name__)

@search.route('/search', methods=['POST'])
@search.route('/search/<query>', methods=['GET'])
def search_tpb(query):
    pass
