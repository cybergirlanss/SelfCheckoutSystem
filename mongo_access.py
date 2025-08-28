from pymongo import MongoClient
def get_database():
    CONNECTION_STRING = "mongodb://localhost:27017"
    client = MongoClient(CONNECTION_STRING)
    dbname = client['Project']
    return dbname['Project.Bill']