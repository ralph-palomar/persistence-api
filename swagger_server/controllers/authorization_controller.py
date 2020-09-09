from typing import List
"""
controller generated to handled auth operation described at:
https://connexion.readthedocs.io/en/latest/security.html
"""
from implementation import processor


def check_APIKeyAuth(api_key, required_scopes):
    return processor.validate_api_key(api_key)


