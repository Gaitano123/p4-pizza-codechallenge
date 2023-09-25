import os
from flask import Flask, make_response,jsonify
from flask_migrate import Migrate
from sqlalchemy_serializer import SerializerMixin
from flask_restful import Resource, Api
from sqlalchemy.orm import validates
from sqlalchemy import MetaData
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///pizza.db"

from api.models import db
from api import routes

migrate = Migrate(app, db)
db.init_app(app)


