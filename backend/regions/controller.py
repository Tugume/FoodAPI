from flask import jsonify,request,Blueprint
from backend.regions.model import Region
from backend.db import db
import datetime
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required


regions =Blueprint('regions',__name__,url_prefix='/regions')

#get all regions
@regions.route('/')
def all_regions():
    regions =Region.query.all()
    return jsonify({
        'success':True,
        'data':regions,
        'total':len(regions)
    }),200

#creating regions
@jwt_required()
@regions.route('/create',methods =['POST'])
def create_new_region():

    data =request.get_json()
    name=data['name']

    #validations
    if not name:
        return jsonify({'error':'Region name is required'})
    if Region.query.filter_by(name=name).first() is not None:
        return jsonify({'error':'Region name exists'}),409
    new_region =Region(name=name,created_at=datetime.now())

    #inserts values
    db.session.add(new_region)
    db.session.commit()
    return jsonify({'message':'New region created successfuuly', 'data':new_region})

#get,edit and delete region by id
@regions.route('/region/<int:id>',methods =['GET','PUT','DELETE'])
def handle_region(id):
    region =Region.query.get_or_404(id)

    if request.method =='GET':
        response ={
            'id':region.id,
            'name':region.name,
            'created_at':region.created_at
        }
        return{'seccess':True, 'region':response,'message':'Region detais retrieved'}
    elif request.method=='PUT':
        data =request.get_json()

        if not data['name']:
            return jsonify({'message':'Region name is required'})
    elif request.method =='DELETE':
        db.session.delete(region)
        db.session.commit()
        return{'message': f'{region.name} region successfully deleted'}  
    elif request.method =='DELETE':
        db.session.delete(region)
        db.session.commit()
        return{'message': f'{region.name} region successfullu deleted'}
      