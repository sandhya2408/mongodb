
import pymongo as pm 
conn = pm.MongoClient("mongodb://localhost:27017")
db = conn["mite"]
collection = db["faculty"]
query = {}
project = {"name":1,"salary":1,"_id":0}
for doc in collection.find().sort("name").limit(3):
    print(f'{doc["name"]} and {doc["salary"]}')


    