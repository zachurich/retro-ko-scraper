# import api
from app.methods import (execute)


def init():
    try:
        # api.init()
        return execute()
    except Exception as e:
        print('Error running scraper', e)
