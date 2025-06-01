from pymongo import MongoClient
from main import token

client = MongoClient(token)

def insert_one(database, column, data):
    db = client[str(database)]
    col = db[str(column)]
    col.insert_one(data)

def update_one(database, column, old, new):
    db = client[str(database)]
    col = db[str(column)]
    col.update_one(old, new)
