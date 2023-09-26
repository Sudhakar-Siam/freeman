import os
from pymongo import MongoClient

conn = MongoClient('mongodb+srv://lddb:lddb123@cluster0.xqdqq1u.mongodb.net/?retryWrites=true&w=majority')
db = conn['freeman_local']

collection_names = db.list_collection_names()

print(collection_names)
print(os.path)