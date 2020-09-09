import logging
import pymongo
import os
from bson.objectid import ObjectId

logger = logging.getLogger('werkzeug')
m_client = pymongo.MongoClient(os.environ['MONGO_SERVER'])
m_db = m_client['persistence']


def insert_data(payload, collection):
    logger.info(payload)
    m_db[collection].insert_one(payload)


def query_all(collection):
    result = list(m_db[collection].find())
    list_of_id = []
    for item in result:
        list_of_id.append(str(item['_id']))
    return list_of_id


def query_one(id, collection):
    logger.info(id)
    result = m_db[collection].find_one({'_id': ObjectId(id)})
    result['_id'] = str(result['_id'])
    return result


def validate_api_key(api_key):
    if api_key == os.environ['API_KEY']:
        return {'test_key': 'test_value'}
    else:
        return None
