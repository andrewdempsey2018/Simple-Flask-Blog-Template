from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

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

@app.route("/delete")
def delete():
    blogId=request.args.get("blogId", None)
    mongo.db.blogscoll.remove({ "_id": ObjectId(blogId) })
    return redirect(url_for("index"))

@app.route("/publish_blog", methods=["POST"])
def publish_blog():
    blogs=mongo.db.blogscoll
    blogs.insert_one(request.form.to_dict())
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)