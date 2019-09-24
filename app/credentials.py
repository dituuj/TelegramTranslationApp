from os import getenv
from pathlib import Path
import os
import json

# TODO: Maybe this is a bad name; consider something related to auth.
class Credentials:
    api_id: str
    api_hash_id: str
    def __init__(self, api_id, api_hash_id):
        self.api_id = api_id
        self.api_hash_id = api_hash_id

    def serialize(self, credentials: Credentials) -> str:
        return json.dumps({"api_id": credentials.api_id,
        "api_hash_id": credentials.api_hash_id})
    
    @staticmethod
    def deserialize(serialized_data: str) -> Credentials: 
        data = json.load(serialized_data)
        return Credentials(data["api_id"], data["api_hash_id"])

def get_credentials() -> Credentials:
    cached_credentials = get_cached_credentials()
    
    api_id = getenv('API_ID')
    api_id_hash = getenv('API_ID_HASH')

    if api_id is None or api_id_hash is None:
        raise Exception('Please store the api key and hash for telegram to use as environment variables API_ID and API_ID_HASH')

    return Credentials(api_id, api_hash_id)




def get_cache_path():
    return Path().absolute()
def get_cache_file_path():
    return os.path.join(get_cache_path(), "password_file")

def cache_credentials(credentials: Credentials):
    cache_file_path = get_cache_file_path()
    #log current dir here
    with open(cache_file_path()) as f:
        f.write(credentials.serialize())

def get_cached_credentials():

    api_id = getenv('API_ID')
    api_id_hash = getenv('API_ID_HASH')

    if api_id is None or api_id_hash is None:
        #todo: alert
        pass
    else:
        return Credentials(api_id, api_id_hash)

    cache_file_path = get_cache_file_path()
    if cache_file_path is None:
        return None
    with open(cache_file_path) as f:
        return Credentials.deserialize(f.read())
