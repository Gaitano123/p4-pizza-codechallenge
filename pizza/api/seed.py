#!/usr/bin/env python3

from faker import Faker
from pizza.app import app
import random

from models import Pizza, Restaurant, RestaurantPizza, db

with app.app_context():
    
    fake = Faker()
    
    Pizza.query.delete()
    Restaurant.query.delete()
    RestaurantPizza.query.delete()
    db.session.commit()
    
    pizzas=[]
    for n in range(70):
        pizza = Pizza(name=fake.name(),
                      ingredients=fake.color_name())
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
        
    restaurant_pizzas = []
    for i in range(100):
        
        random_pizza = random.choice(pizzas)
        random_restaurant = random.choice(restaurants)
        
        restaurant_pizza = RestaurantPizza(
            pizza_id = random_pizza.id,
            restaurant_id = random_restaurant.id,
            price = random.randint(1, 30)
        )
        restaurant_pizzas.append(restaurant_pizza)
    db.session.add_all(restaurant_pizzas)
    db.session.commit()        