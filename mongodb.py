import pymongo


client = pymongo.MongoClientmongodb+srv://pbilakshan:AltruixUB@userbot.gdno4qt.mongodb.net/?retryWrites=true&w=majority")


db = client["Hashira"]

 with your collection name)
collection = db["Default_1"]


data = {"key": "value"}
collection.insert_one(data)


result = collection.find({"key": "value"})


for document in result:
    print(document)


client.close()
