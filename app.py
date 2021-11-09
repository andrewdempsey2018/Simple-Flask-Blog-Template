from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

import os

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://andrew2021:wildside1@andrewcluster.igjjx.mongodb.net/blogsdb?retryWrites=true&w=majority"
mongo = PyMongo(app)

#connect to the database using heroku env variable
#app.config["MONGO_URI"] = os.getenv("MONGO_URI")

# blog data references the collection within mongo db atlas that holds the blog data
blogData = mongo.db.blogscoll

@app.route("/")
def index():
    return render_template("index.html", blogs = blogData.find())

@app.route("/create")
def create():
    return render_template("create.html")

@app.route("/edit")
def edit():
    blogId=request.args.get("blogId", None)
    return render_template("edit.html", blog=blogData.find_one({ '_id': ObjectId(blogId)}))

@app.route("/delete")
def delete():
    blogId=request.args.get("blogId", None)
    blogData.remove({ "_id": ObjectId(blogId) })
    return redirect(url_for("index"))

@app.route("/publish_blog", methods=["POST"])
def publish_blog():
    blogs=blogData
    blogs.insert_one(request.form.to_dict())
    return redirect(url_for('index'))

@app.route('/edit_blog', methods=["POST"])
def edit_blog():
    blogId=request.args.get('blogId', None)
    blogs = blogData
    blogs.update( {'_id': ObjectId(blogId)},
    {
        'title':request.form.get('title'),
        'text':request.form.get('text'),
    })
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)