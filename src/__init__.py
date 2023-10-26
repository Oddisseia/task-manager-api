from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from src.config import config

database = SQLAlchemy()


def create_app(config_type):
    app = Flask(__name__)
    app.config.from_object(config[config_type])
    database.init_app(app)
    return app
