#!/usr/bin/env python3

from flask import Flask, request, make_response, jsonify
from flask_restful import Api, Resource
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from models import Pizza, Restaurant,RestaurantPizza, db

app = Flask(__name__)
api= Api(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///pizza.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)

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
            restaurant_dict = restaurant.to_dict()
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
  
    
if __name__ == '__main__':
    app.run(port=5555, debug=True)

# @app.route('/')
# def index():
#     return '<h1>Pizza and Restaurant GET API</h1>'

# @app.route('/restaurants', methods=['GET', 'POST'])
# def restaurant():

#     if request.method == 'GET':
#         restaurants = Restaurant.query.all()
#         restaurant_list=[]
    
#         for restaurant in restaurants:
#             restaurant_dict = {
#                 "id": restaurant.id,
#                 "name": restaurant.name,
#                 "address": restaurant.address,
#             }
#             restaurant_list.append(restaurant_dict)
    
#         response = make_response(jsonify(restaurant_list), 200)
        
#         return response
    
#     elif request.method == 'POST':
#         new_restaurant = Restaurant(
#             name = request.form.get('name'),
#             address = request.form.get('address'),
#         )
#         db.session.add(new_restaurant)
#         db.session.commit()
        
#         response_dict = new_restaurant.to_dict()
#         response = make_response(jsonify(response_dict), 201)
#         return response
    
    
# @app.route('/restaurants/<int:id>', methods=['GET', 'DELETE'])
# def restaurant_id(id):
    
#     restaurant = Restaurant.query.filter(Restaurant.id == id).first()
    
#     if not restaurant:
#         response = make_response(jsonify({"error": "Restaurant not found"}), 404)

#     if request.method == 'GET': 
#         if not restaurant:
#             response = make_response(jsonify({"error": "Restaurant not found"}), 404)
                
#         restaurant_dict = restaurant.to_dict()
#         response =make_response(jsonify(restaurant_dict), 200)
        
#         return response
    
#     if request.method == 'DELETE':
        
#         if not restaurant:
#             response = make_response(jsonify({"error": "Restaurant not found"}), 404)
        
#         db.session.delete(restaurant)
#         db.session.commit()
        
#         response = make_response(jsonify({"message": "Restaurant deleted"}), 200)
        
#         return response
    
# @app.route('/pizzas', methods=['GET', 'POST'])
# def pizza():
#     if request.method == 'GET':
#         pizzas = Pizza.query.all()
#         pizzas_list = []
        
#         for pizza in pizzas:
#             pizza_dict = {
#                 "id": pizza.id,
#                 "name": pizza.name,
#                 "ingredients": pizza.ingredients,
#             }
#             pizzas_list.append(pizza_dict)
        
#         response = make_response(jsonify(pizzas_list), 200)
        
#         return response
    
    
#     if request.method == 'POST':
#         new_pizza = Pizza(
#             name = request.form.get('name'),
#             ingredients = request.form.get('ingredients'),
#         )
#         db.session.add(new_pizza)
#         db.session.commit()
        
#         pizza_dict = new_pizza.to_dict()
#         response = make_response(jsonify(pizza_dict), 201)
#         return response
    
# @app.route('/restaurant_pizza', methods=['POST'])
# def restaurant_pizza():
#     new_record = RestaurantPizza(
#         price = request.form.get('price'),
#         pizza_id = request.form.get('pizza_id'),
#         restaurant_id = request.form.get('restaurant_id')
#     )
#     db.session.add(new_record)
#     db.session.commit()
    
#     record_dict = new_record.to_dict()
#     response = make_response(jsonify(record_dict), 201)
    
#     return response
    
