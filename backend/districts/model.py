from backend.db import db
from dataclasses import dataclass

@dataclass
class District(db.Model):
    __tablename__='districts'
    name:str
    region_id:int


    id =db.Column(db.Integer,primary_key=True)
    name =db.Column(db.String(255),unique=True)
    region_id = db.Column(db.Integer,db.ForeignKey('regions.id'))
    created_by  = db.Column(db.Integer,db.ForeignKey('users.id'))
    created_at =db.Column(db.String(255), nullable=True)
    updated_at =db.Column(db.String(255), nullable=True)
    adresses = db.relationship("Address",backref="district")


    def __init__(self,name, region_id, created_by, created_at,udpated_at):
     self.region_id = region_id
     self.name = name
     self.created_by = created_by
     self.created_at=created_at
     self.updated_at=udpated_at


    def __repr__(self):
       return f'<District {self.name}>'