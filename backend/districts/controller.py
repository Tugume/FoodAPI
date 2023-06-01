from flask import jsonify,request,Blueprint
from backend.districts.model import District
from backend.db import db
import datetime
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required


districts =Blueprint('districts',__name__,url_prefix='/districts')

#get all districts
@districts.route('/')
def all_districts():
    districts =District.query.all()
    return jsonify({
        'success':True,
        'data':districts,
        'total':len(districts)
    }),200

#creating districts
@jwt_required()
@districts.route('/create',methods =['POST'])
def create_new_districts():
    data=request.get_json()
    region_id=data['region_id']
    name=data['name']
    created_by =get_jwt_identity()


    #validations
    if not name:
        return jsonify({'error':'District name is required'})
    if not region_id:
        return jsonify({'error':'District region name is required'})
    if District.query.filter_by(name=name).first() is not None:
        return jsonify({'error':'District name exists'}),409
    
    new_district =District(name=name, created_by =created_by,created_at=datetime.now())

    #inserting values
    db.session.add(new_district)
    db.session.commit()
    return jsonify({'message': 'New district created successfully','data':new_district}),201

#get,edit and delete district by id
@districts.route('/district/<int:id>',methods =['GET','PUT','DELETE'])
def handle_districts(id):
    
    if request.method =='GET':
        response={
            'id':district.id,
            'name':district.name,
            'region':district.region.name,
            'created_by':district.created_by,
            'created_at':district.created_at

        }