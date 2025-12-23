from flask import Flask, redirect, render_template, request, Blueprint, url_for, session
from bson.objectid import ObjectId
from app import mongo

tasks_bp = Blueprint('tasks', __name__)

@tasks_bp.route("/", methods = ["GET", "POST"])
def home():
    # Redirect users to login if not authenticated
    if 'user' not in session:
        return redirect(url_for("auth.login"))

    # Example: retrieve tasks for the logged-in user. Adjust the query to match your schema.
    user_data = mongo.db.users.find_one({"username": session.get('user')})
    
    if not user_data:
        return redirect(url_for("auth.logout"))
    task_cursor = mongo.db.tasks.find({"userID": user_data['_id']}) #this is wrong it only returns single dictionary but we need all so user find() instead of find_one()
    print(task_cursor)

    return render_template("tasks.html", tasks=task_cursor)

@tasks_bp.route("/add", methods = ["POST"])
def add():
    if 'user' not in session:
        redirect(url_for("auth.login"))
    
    user_data = mongo.db.users.find_one({"username": session["user"]})
    task = {
        "userID": user_data['_id'],
        "task":request.form.get("task"),
        "complete": False
    }
    mongo.db.tasks.insert_one(task)
    return redirect(url_for("tasks.home"))
    
    
@tasks_bp.route("/toggle/<task_id>", methods = ["POST"])
def toggle(task_id):
    if 'user' not in session:
        redirect(url_for("auth.login"))
        
    mongo.db.tasks.update_one(
    {"_id": ObjectId(task_id)},      # FILTER: Find the document with this ID
    {"$set": {"complete": True}})     # UPDATE: Change only the 'status' field
    return redirect(url_for("tasks.home"))
    
    
@tasks_bp.route("/delete/<task_id>", methods = ["POST"])
def delete(task_id):
    if 'user' not in session:
        redirect(url_for("auth.login"))
        
    mongo.db.tasks.delete_one({"userID": ObjectId(task_id)})
    return redirect(url_for("tasks.home"))
    
    
    

        
    
    