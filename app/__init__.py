from flask import Flask
from flask_pymongo import PyMongo

mongo = PyMongo()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'SecretKey123'
    app.config['MONGO_URI'] = 'mongodb://localhost:27017/todo_db'
    mongo.init_app(app)
    
    from app.routes.auth import auth_bp
    from app.routes.tasks import tasks_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(tasks_bp)
    
    return app
