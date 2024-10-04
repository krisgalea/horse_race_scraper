from pymongo import MongoClient

class DatabaseClient:

    db = None

    def __init__(self, hostname = "localhost", port = 27017, databaseName = "test"):
        self.db = MongoClient(hostname, port)[databaseName]
        print "connected to db with hostname: [", hostname, "]"

    def findById(self, collectionName, targetId):
        print "searching for item from db under collection name: [ ", collectionName, "]"
        if (collectionName is not None & targetId is not None):
            return self.db[collectionName].find_one({"_id":targetId})
        else :
            raise ValueError("missing params")

    def findByField(self, collectionName, fieldName, fieldValue):
        print "searching for item from db under collection name: [ ", collectionName, "] for field [", fieldName, "] having value [", fieldValue, "]"
        if (collectionName is not None & fieldName is not None & fieldValue is not None):
            return self.db[collectionName].find_one({fieldName : fieldValue})
        else :
            raise ValueError("missing params")

    def insertOne(self, collectionName, item):
        print "inserting one item"
        return self.db[collectionName].insert_one(item)

    def insertMany(self, collectionName, items):
        print "inserting many items"
        return self.db[collectionName].insert_many(items)
