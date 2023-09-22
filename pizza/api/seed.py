#!/usr/bin/env python3

from faker import Faker
from app import app

from models import Pizza, RestaurantPizza, Restaurant, db

with app.app_context():
    
    fake = Faker()
    
    Pizza.query.delete()
    Restaurant.query.delete()
    RestaurantPizza.query.delete()
    
    pizzas=[]
    for n in range(70):
        pizza = Pizza(name=fake.name(),
                      ingredients=fake.ingredients())
        pizzas.append(pizza)
        
        db.session.add_all(pizzas)
        db.session.commit()
        
    restaurants = []
    for n in range(70):
        restaurant = Restaurant(name= fake.name(),
                                address = fake.address())
        restaurants.append(restaurant)
        
        db.session.add_all(restaurants)
        db.session.commit()