import logging
import pymongo
import os

logger = logging.getLogger('werkzeug')
m_client = pymongo.MongoClient('mongodb://localhost:27017/')
m_db = m_client['persistence']


def insert_data(payload, collection):
    logger.info(payload)
    m_db[collection].insert_one(payload)


def validate_api_key(api_key):
    if api_key == os.environ['API_KEY']:
        return {'test_key': 'test_value'}
    else:
        return None
