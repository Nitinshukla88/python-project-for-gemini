from flask import Flask 

app = Flask(__name__)

users = {"nitin" : "shukla"}

@app.get("/")
def hello():
    return "Hello world"

@app.post("/set-name/<first>/<last>")
def setName(first, last):
    users[first] = last
    return "lastName entered successfully"
@app.get("/get-name/<first>")
def getName(first):
    if first not in users:
        return "Enter a valid firstName"
    else:
        return users[first]

