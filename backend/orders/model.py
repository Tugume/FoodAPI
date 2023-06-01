from backend.db import db

class Order(db.Model):
    __tablename__='orders'
    id =db.Column(db.Integer,primary_key=True)
    quantity=db.Column(db.Integer)
    location =db.Column(db.String(255),nullable=False)


def __init__(self, quantity, location):
 self.quantity =quantity
 self.location =location


def __repr__(self):
   return f'<order{self.user_id}>'




