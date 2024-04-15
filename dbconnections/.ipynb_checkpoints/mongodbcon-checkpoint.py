# pip install pymongo

from pymongo import MongoClient

def connect_to_mongodb(username, password, cluster_name):
    try:
        # Construct MongoDB URI dynamically
        uri = f"mongodb+srv://{username}:{password}@{cluster_name}.mongodb.net/"

        # Create a new client and connect to the server
        client = MongoClient(uri, tls=True)

        # Send a ping to confirm a successful connection
        client.admin.command('ping')

        print("Pinged your deployment. You successfully connected to MongoDB!")

        return client
    
    except Exception as e:
        print(e)
        return None