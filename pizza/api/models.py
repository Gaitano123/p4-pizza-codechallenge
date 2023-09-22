# from . import db
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from sqlalchemy.orm import validates
from datetime import datetime

db = SQLAlchemy()

class Restaurant(db.Model):
    
    __tablename__ = 'restaurants'
    
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), unique=True)
    address = db.Column(db.String())
    
    pizza = db.relationship('RestaurantPizza', backref='restaurant')
    
    @validates('name')
    def validate_name(self, key, name):
        if len(name) > 50:
            raise ValueError('name must be at least 50 characters')
        
        return name


class Pizza(db.Model):
    
    __tablename__ = 'pizzas'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    ingredients = db.Column(db.String())
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    
    restaurant = db.relationship('RestaurantPizza', backref='pizza')
    

class RestaurantPizza(db.Model):
    
    __tablename__ = 'restaurants_pizza'
    
    id = db.Column(db.Integer, primary_key=True)
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizzas.id'))
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'))
    price = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    
    @validates('price')
    def validate_price(self, key, amount):
        if not (1 <= amount <=30):
           raise ValueError('Amount must be between 1 and 30')
        
        return amount 
