import os
import urllib

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




##########################################
# FOR MONGODB WITH NO AUTHENTICATION.
# COMMENT THE BELOW BLOCK & UNCOMMENT NEXT 
# BLOCK IF YOU USE USERNAME & PASSWORD
##########################################

# Set connection url to connect
# Example: "mongodb://13.233.190.38:27017/"
connection_url = 'mongodb://%s:%s/' % (host, port)
mongo = pymongo.MongoClient(connection_url)


##########################################
# FOR MONGODB WITH AUTHENTICATION.
# UNCOMMENT THE BELOW CODE BLOCK & COMMENT 
# PREVIOUS CODE BLOCK.
##########################################

# username=urllib.parse.quote_plus(os.getenv('username')) 
# password=urllib.parse.quote_plus(os.getenv('password'))

# connection_url = 'mongodb://%s:%s@%s:%s/' % (username, password, host, port)
# mongo = pymongo.MongoClient(connection_url)

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
db = mongo[database]

# Get a collection that exist or create a new collections
# Collections are like tables in MySQL and stores data as documents(somewhat like rows)
# Note: Collection will not be created until first set of data is written.
users_collection = db["user"]

# Insert a sample user data to user collections

# Sample user data (dict)
user_data = { "name": "John", "address": "Highway 37" }

# Insert the data to users_collection
res = users_collection.insert_one(user_data)

# Print Response 
print(res.inserted_id)

