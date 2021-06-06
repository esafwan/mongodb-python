import os

#import pymongo library to access mongodb 
import pymongo

#Import dotenv library to read sensitive info from .env file
from dotenv import load_dotenv

#load values of .env file.
load_dotenv()

host=os.getenv('host')
port=os.getenv('port')
database=os.getenv('database')

mongo = pymongo.MongoClient("mongodb://13.233.190.38:27017/")



#Get list of all databases from mongodb
dblist = mongo.list_database_names()

#Check if db exist
if "safwan" in dblist:
  print("The database exists.")
else:
  print("The database doesn't exists. See available dbs below:")
  print(dblist)
