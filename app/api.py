import falcon
from methods import (List, List_Available)


def init():
    api = falcon.API()

    api.add_route('/list-all', List())
    api.add_route('/list-available', List_Available())
