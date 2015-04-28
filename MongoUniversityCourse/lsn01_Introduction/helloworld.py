##encoding=utf8

import pymongo
from pymongo import MongoClient

conn = MongoClient("localhost", 27017)
db = conn.test
things = db.things

# things.save({"a": 3, "b": 2, "c":1})
for item in things.find():
    print(item)