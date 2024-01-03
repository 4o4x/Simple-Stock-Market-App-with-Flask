from flask import Flask
from pymongo import MongoClient


def create_app():
    app = Flask(__name__)
    app.secret_key = 'super_secret_key'

    # MongoDB bağlantısı
    app.db = MongoClient("mongodb+srv://bur:bur123@cluster0.yk35zgk.mongodb.net/?retryWrites=true&w=majority")["test"]

    from .routes.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .routes.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
