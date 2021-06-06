import os

# import pymongo library to access mongodb 
import pymongo

# Import dotenv library to read sensitive info from .env file
from dotenv import load_dotenv

# Load values of .env file.
load_dotenv()

# Set variables from .env variables
host=os.getenv('host')
port=os.getenv('port')
database=os.getenv('database')

# Set connection url to connect
# Example: "mongodb://13.233.190.38:27017/"
connection_url = "mongodb://" + host + ":" + "27017/"
mongo = pymongo.MongoClient(connection_url)

# Get list of all databases from mongodb
dblist = mongo.list_database_names()

# Check if db exist
if "safwan" in dblist:
  print("The database exists.")
  
else:
  print("The database doesn't exists. See available dbs below:\n")
  print(dblist)


# Connect to existing DB or create DB.
# Note: Database will not be created until first set of data is written.
db = mongo["safwan"]

# Get a collection that exist or create a new collections
# Collections are like tables in MySQL and stores data as documents(somewhat like rows)
# Note: Collection will not be created until first set of data is written.
users_collection = db["user"]

# Insert a sample user data to user collections

# Sample user data (dict)
user = { "name": "John", "address": "Highway 37" }

# Insert the data to users_collection
res = users_collection.insert_one(user)

# Print Response 
print(res.inserted_id)

