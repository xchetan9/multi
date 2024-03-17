# app/__init__.py
from flask import Flask
from .routes import api

def create_app():
    app = Flask(__name__)
    app.register_blueprint(api)
    return app
