import pymongo
import json
import bson
try:
    conn=pymongo.MongoClient('mongodb://172.25.0.50:27017/?replicaSet=rs1')
except:
    print("failed to connect")
db=conn['sirix']
col=db['RelatedAccounts']
data=()
print("Adding documents to \m" ,col)
my_dict={"UserId": "NumberInt(3473343)","Group" : "Marbella"}
col.insert_one(my_dict)
