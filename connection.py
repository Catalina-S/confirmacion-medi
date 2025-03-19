from pymongo import MongoClient
from pymongo.server_api import ServerApi


def connect_to_mongodb(db_name, collection_name):
    uri = "mongodb+srv://catalinasanchezm:F0LmP240@samplepatientservice.khioc.mongodb.net/?retryWrites=true&w=majority&appName=SamplePatientService"
    client = MongoClient(uri, server_api=ServerApi('1'))
    db = client[db_name]
    collection = db[collection_name]
    return collection
