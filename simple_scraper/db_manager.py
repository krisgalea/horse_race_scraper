from db import DatabaseClient

class DbManager:

    DB_HOST = 'localhost'
    DB_PORT = 27017
    DB_COLLECTION_NAME = "TestMe"

    def __init__(self):
        print self.DB_PORT
        self.dbClient = DatabaseClient(self.DB_HOST, self.DB_PORT)

    def addItem(self, item):
        return self.dbClient.insertOne(self.DB_COLLECTION_NAME, item.__dict__)

    def findOne(self, id):
        return self.dbClient.findById(self.DB_COLLECTION_NAME, id)
