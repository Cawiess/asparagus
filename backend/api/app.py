import os

from flask import Flask
from flask_smorest import Api

def create_app(db_url=None):
    app = Flask(__name__)

    # add app.config[]
    # connect app to database
    # create tables
    # connect app object with flask smorest api functionality
    # register blueprints

    return app