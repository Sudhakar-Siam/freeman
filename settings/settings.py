import os
from pymongo import MongoClient


conn = MongoClient('mongodb+srv://lddb:lddb123@cluster0.xqdqq1u.mongodb.net/?retryWrites=true&w=majority')
db = conn[os.getenv('DB_NAME')]
