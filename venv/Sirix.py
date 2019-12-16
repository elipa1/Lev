from SirixDBConnector import MongoConnect
import pymongo
import json
MongoConnect()
db='sirix'
try: {
    db.RelatedAccounts.insertMany([
        {"UserId": NumberInt(3473343)},
        {"Group" : "Marbella"}])
}
except pymongo:
    print("Failed to add")


