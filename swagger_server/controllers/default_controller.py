import connexion
import six

from swagger_server import util
from implementation import processor


def modify_id_put(id, collection):  # noqa: E501
    """modify_id_put

    Update data by specified ID from the collection # noqa: E501

    :param id: 
    :type id: str
    :param collection: 
    :type collection: str

    :rtype: None
    """
    return 'do some magic!'


def remove_id_get(id, collection):  # noqa: E501
    """remove_id_get

    Delete data by specified ID from the collection # noqa: E501

    :param id: 
    :type id: str
    :param collection: 
    :type collection: str

    :rtype: None
    """
    return 'do some magic!'


def retrieve_get(collection):  # noqa: E501
    """retrieve_get

    Retrieve all data from the collection # noqa: E501

    :param collection: 
    :type collection: str

    :rtype: List[object]
    """
    return processor.query_all(collection)


def retrieve_id_get(id_, collection):  # noqa: E501
    """retrieve_id_get

    Retrieve data by specified ID from the collection # noqa: E501

    :param id: 
    :type id: str
    :param collection: 
    :type collection: str

    :rtype: object
    """
    return processor.query_one(id_, collection)


def save_post(collection, body=None):  # noqa: E501
    """save_post

    Saves data to the specified collection name # noqa: E501

    :param collection: 
    :type collection: str
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = connexion.request.get_json()  # noqa: E501
        processor.insert_data(body, collection)
    return None, 201
