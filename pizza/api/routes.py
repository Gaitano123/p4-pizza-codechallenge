#!/usr/bin/env python3

from flask import Flask, request, make_response, jsonify
from flask_restful import Api, Resource
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from api.models import Pizza, Restaurant,RestaurantPizza, db
from api import api 

class Index(Resource):
    
    def get(self):
        response = {"message": "PIZZA AND RESTAURANT API"}
        return make_response(response, 200)

api.add_resource(Index, '/')


class Restaurants(Resource):
    
    def get(self):
        restaurants = Restaurant.query.all()
        restaurant_list=[]
        for restaurant in restaurants:
            restaurant_dict = {
                "id": restaurant.id,
                "name": restaurant.name,
                "address": restaurant.address,
            }
            restaurant_list.append(restaurant_dict)
        response = make_response(jsonify(restaurant_list), 200)
        return response
    
    def post(self):
        new_restaurant = Restaurant(
            name = request.form.get('name'),
            address = request.form.get('address'),
        )
        db.session.add(new_restaurant)
        db.session.commit()
        
        response_dict = new_restaurant.to_dict()
        response = make_response(jsonify(response_dict), 201)
        return response
    
api.add_resource(Restaurants, '/restaurants')


class RestaurantById(Resource):
    
    def  get(self, id):
        restaurant = Restaurant.query.filter(Restaurant.id == id).first()
        if restaurant:
            restaurant_dict ={
                "id": restaurant.id,
                "name": restaurant.name,
                "address": restaurant.address,
            }
            response =make_response(jsonify(restaurant_dict), 200)
        else:        
            response = make_response(jsonify({"error": "Restaurant not found"}), 404)
        return response
    
    def delete(self, id):
        restaurant = Restaurant.query.filter(Restaurant.id == id).first()
        if restaurant:
            db.session.delete(restaurant)
            db.session.commit()
            response = make_response(jsonify({"message": "Restaurant deleted"}), 200)
        else:       
            response = make_response(jsonify({"error": "Restaurant not found"}), 404)
        return response
    
api.add_resource(RestaurantById, '/restaurantbyid/<int:id>')


class Pizzas(Resource):
    
    def get(self):
        pizzas = Pizza.query.all()
        pizzas_list = []
        
        for pizza in pizzas:
            pizza_dict = {
                "id": pizza.id,
                "name": pizza.name,
                "ingredients": pizza.ingredients,
            }
            pizzas_list.append(pizza_dict)
        
        response = make_response(jsonify(pizzas_list), 200)
        
        return response
    
api.add_resource(Pizzas, '/pizzas')


class RestaurantPizzas(Resource):
    def post(self):
        new_record = RestaurantPizza(
        price = request.form.get('price'),
        pizza_id = request.form.get('pizza_id'),
        restaurant_id = request.form.get('restaurant_id')
        )
        db.session.add(new_record)
        db.session.commit()
        
        record_dict = new_record.to_dict()
        response = make_response(jsonify(record_dict), 201)
        
        return response
    
api.add_resource(RestaurantPizzas, '/restaurantpizzas')