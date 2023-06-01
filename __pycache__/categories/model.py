from backend.db import db
from dataclasses import dataclass


@dataclass
class Category(db.Model):
    __tablename__='categories'

    name:str
    image:str
    id =db.Column(db.Integer, primary_key =True)
    name =db.Column(db.String(255),unique =True)
    image =db.Column(db.String(255),nullable=False)
    created_by =db.Column(db.Integer,db.ForeignKey('users.id'))
    created_at =db.Column(db.String(255),nullable=True)
    updated_by =db.Column(db.String(255),nullable=True)

def __init__(self,name,image,created_at,updated_at,created_by):
    self.name =name
    self.image =image
    self.created_by = created_by
    self.created_at =created_at
    self.updated_at =updated_at

    def __repr__(self):
       return f'<User{self.name}>'
    
  