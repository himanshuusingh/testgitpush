import pymongo
client = pymongo.MongoClient("mongodb+srv://Himan_1997:himan_1997@himanshu18.ysbsqux.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name":"himanshu",
    "email" : "himanshu@ineuron.ai",
    "surname" : "kumar"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d )