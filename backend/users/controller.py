from flask import jsonify, request,Blueprint
from backend.users.model import User
from backend.db import db
import datetime
from werkzeug.security import generate_password_hash


users =Blueprint('users',__name__,url_prefix ='/users')

#get all users
@users.route('/')
def all_users():
    users =User.query.all()
    return jsonify({
        'sucess':True,
        'data':users,
        'total':len(users)
    }),200
#get author books
@users.route('/author/<int:id>/books')
def get_all_author_books(id):
    user =User.query.filter_by(id-id).first()
    books =user.books
    return jsonify({
        'success':True,
        'data':books,
        'total':len(users)
    }),200
@users.route('/user/<user_id>',methods=['GET','PUT','DELETE'])
def handle_user(user_id):
    user=User.query.get_or_404(user_id)

    if request.method =='GET':
        response ={
            'id':user.id,
            'name':user.name,
            'user_type':user.user_type,
            'email':user.email,
            'contact':user.contact
        }
        return{'success':True,'user':response,'message':'user details retrieved'}
    elif request.method =='PUT':
        data =request.get_json()

        #validations
        if not data['name']:
            return jsonify({'message':'Your name is required'})
        if not data['email']:
            return jsonify({'message':'Your email address is required'})
        if not data['contact']:
            return jsonify({'message':'Your contact is required'})
        if not data['password']:
            return jsonify({'message':'Your password is required and mus be greater than 6 characters'})
        
        user.name =data['name']
        user.email =data['email']
        user.contact =data['contact']
        user.password =generate_password_hash(data['password'])
        user.updated_at =datetime.utcnow()
        db.session.add(user)
        db.session.commit()
        return {'message':f'User details of {user.name} updated successfully'}
    elif request.method =='DELETE':
        db.session.delete(user)
        db.session.commit()
        return {'message': f'{user.name} successfully deleted'}
    
#get user books
@users.route('/user/<user_id>/books', methods =['GET'])
def user_books(user_id):
    user =User.query.get_or_404(user_id)
    books =user.books
    return jsonify({'message':'Use book'})

        
