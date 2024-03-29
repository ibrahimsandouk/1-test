from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

db = SQLAlchemy()


class Men(db.Model):
    __tablename__ = 'mens'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))

    def json(self):
        return {"id": self.id, "name": self.name}

class Employee(db.Model):
    __tablename__ = 'Employee'
    id = db.Column(db.Integer ,primary_key=True)
    name = db.Column(db.String(120))
    #position_id = db.Column(db.Integer ,ForeignKey('position.id'))
    #position = relationship('Position')
    building_id= db.Column(db.Integer ,ForeignKey('Building.id'))
    building=relationship('Building')

    def json(self):
        return {"id": self.id, "name": self.name,"building":self.building.json()}

class Position(db.Model):
    __tablename__ ='position'
    id = db.Column(db.Integer ,primary_key=True)
    name = db.Column(db.String(120))

    def json(self):
        return {"id": self.id, "name": self.name}

class Building(db.Model):
    __tablename__ = 'Building'
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(120))
    name = db.Column(db.String(120))

    def json(self):
        return {"id": self.id, "address": self.address,"name": self.name}

