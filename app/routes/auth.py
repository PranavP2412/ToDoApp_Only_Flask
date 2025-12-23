from flask import Flask, session, redirect, Blueprint, url_for, render_template, request, flash
from app import mongo

auth_bp = Blueprint('auth', __name__)

USER_CREDENTIALS = {
    'name' :'admin',
    'password' :'123'
}

@auth_bp.route('/register',methods = ["POST", "GET"])
def register():
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
        user = {
            "username": username,
            "password": password
        }
        
        mongo.db.users.insert_one(user)
        return redirect(url_for("auth.login"))
        
    return render_template("register.html")


@auth_bp.route('/login',methods = ["POST", "GET"])
def login():
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
        user = mongo.db.users.find({"username": username})
        
        if user:
            session['user'] = username
            flash('Login Successful!!','success')
        else:
            flash("Entered wrong username or password or you have not registered yet.")
        return redirect(url_for("tasks.home"))
        
    return render_template("login.html")

@auth_bp.route("/logout", methods = [ "GET" ,"POST"])
def logout():
    session.pop("user")
    flash("logged out successfully","info")
    return redirect(url_for('auth.login'))
        

