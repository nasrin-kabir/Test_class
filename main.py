import os
from dotenv import load_dotenv 

# Load environment variables

load_dotenv()
API_KEY = os.getenv("API_KEY")
databaseurl2 = os.getenv("database_url")
print(API_KEY)
print(databaseurl2)
print ("Hello new branch")
