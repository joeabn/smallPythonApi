import uvicorn
from fastapi import FastAPI
import sqlite3
import os
from pydantic import BaseModel
import pymongo

app = FastAPI()
db = os.environ['db']
url = os.environ['url']
port = os.environ['port']

#db = "testdb"
#url = "localhost"
#port = 27017

# mongodb://localhost:27017
class PERSON(BaseModel):
    name: str
    

    
mycol = None

@app.get("/connect")
def connect():
    global mycol
    myclient = pymongo.MongoClient(url + ":" + str(port))
    
    if db not in myclient.list_database_names():
        myclient[db]
       
    mydb = myclient[db]
    mycol = mydb["Community"]
    
    return "Connected"

@app.get("/hello")
def hello():
    return {"Hello": "World"}

@app.get("/Community")
def read_item():
    result = []
    for x in mycol.find():
        result.append(x["name"])
    return result
    
@app.post("/Community")
async def create_item(pers: PERSON):
    
    x = mycol.insert_one(dict(pers))

    return "Added !"

@app.delete("/Community")
async def delete_all():
    mycol.delete_many({})
    return "Success!"
    
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
    
