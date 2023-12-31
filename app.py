from flask import Flask, render_template, request
import subprocess as sp
from pymongo import MongoClient
from mongopass import mongopass

app = Flask(__name__)

client = MongoClient(mongopass)
db = client.crud
myCollection = db.myColl


@app.route("/")
def my_home():
    date = sp.getoutput("date /t")
    return render_template("/home.html", date=date)

@app.route("/crud")
def curd():
    return render_template("/crud.html")

@app.route("/read")
def read():
    corsor = myCollection.find()
    for record in cursor:
        name = record["name"]
        print(record)
    return render_template("/response.html", res=name)

@app.route("/insert")
def insert():
    name = request.args.get("name")
    address = request.args.get("address")
    myVal = {"name": name, "address": address}
    x = myCollection.insert_one("/response.html", res = x)

@app.route("/delete")
def delete():
    name = request.args.get("name")
    myquery = {"name": name}
    x = myCollection.delete_one("/response.html", res = x)

@app.route("/update")
def update():
    name = request.args.get("name")
    new_address = request.args.get("new_address")
    myquery = {"name": name}
    newvalues = {"$set": {"address" : new_address}}
    myCollection.update_one(myquery, newvalues)
    x = "Record updated"
    return render_template("/response.html", res = x)

if (__name__) == "main":
    app.run(Debug = True)