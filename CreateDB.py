import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

#db = myclient.mydatabase
#collection = db.mycollection

mydb = myclient["mydatabase"]

print(myclient.list_database_names())

dblist = myclient.list_database_names()
if "mydatabase" in dblist:
  print("The database exists.")
else:
  print("The database does not exist.")