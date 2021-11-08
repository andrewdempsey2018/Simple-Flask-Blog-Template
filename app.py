from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo

import os

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://andrew2021:wildside1@andrewcluster.igjjx.mongodb.net/testdb?retryWrites=true&w=majority"
mongo = PyMongo(app)

#connect to the database using heroku env variable
#app.config["MONGO_DBNAME"] = "IGF_DB"
#app.config["MONGO_URI"] = os.getenv("MONGO_URI")
#make an instance of PyMongo and pass the app in


#load the home page along with a cursor containing all games currently in the database
@app.route("/")
def get_games():
    return render_template("index.html")

@app.route("/text")
def text():
    return render_template("text.html", data = mongo.db.testcolls.find_one())

if __name__ == '__main__':
    app.run(debug=True)