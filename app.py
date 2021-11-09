from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo

import os

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://andrew2021:wildside1@andrewcluster.igjjx.mongodb.net/blogsdb?retryWrites=true&w=majority"
mongo = PyMongo(app)

#connect to the database using heroku env variable
#app.config["MONGO_URI"] = os.getenv("MONGO_URI")

@app.route("/")
def index():
    return render_template("index.html", blogs = mongo.db.blogscoll.find())

@app.route("/create")
def create():
    return render_template("create.html")

if __name__ == '__main__':
    app.run(debug=True)