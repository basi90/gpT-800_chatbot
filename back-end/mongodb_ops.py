import pymongo


class MongoDBOperations:
    # Initializes the MongoDB connection and sets the specified database and collection
    def __init__(self, connection_file_path, database_name, collection_name):
        with open(connection_file_path) as file:
            self.connection_string = file.read().strip()
        self.client = pymongo.MongoClient(self.connection_string)
        self.db = self.client[database_name]
        self.collection = self.db[collection_name]

    # Saves the user input and bot response to the MongoDB collection
    def save_to_db(self, user_input, bot_response):
        chat = {"user_input": user_input, "bot_response": bot_response}
        self.collection.insert_one(chat)

    # Closes the MongoDB connection
    def close_connection(self):
        self.client.close()
