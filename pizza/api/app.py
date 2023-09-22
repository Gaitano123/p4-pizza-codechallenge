#!/usr/bin/env python3

from flask import Flask, request, make_response
from flask_restful import Api
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from models import Pizza, Restaurant, RestaurantPizza, db

app = Flask(__name__)
api= Api(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///pizza.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)

api = Api(app)