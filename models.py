from app import db
from datetime import datetime

class Admin(db.Model):

    __tablename__ = 'Admin'
    
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    password = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return '<username %r>' % self.username

class Product(db.Model):

    __tablename__ = 'Product'
    
    id = db.Column(db.Integer,primary_key=True)
    category = db.Column(db.String(200), nullable=False)

class Catalog(db.Model):

    __tablename__ = 'Catalog'
    
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=True)
    category = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Float, nullable=False)
    image = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)
