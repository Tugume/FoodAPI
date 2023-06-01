from flask import Blueprint,request,jsonify
from backend.db import db
from backend.food_items.model import FoodItem
import datetime


food_items =Blueprint('food_items',__name__, url_prefix='/food_items')

#get all companies
@food_items.route('/')
def all_food_items():
    companies =FoodItem.query.all()
    return jsonify({'success':True,'data':companies,'total':len(companies)}),200