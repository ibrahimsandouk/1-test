from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Men(db.Model):
    __tablename__ = 'mens'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))

    def json(self):
        return {"id": self.id, "name": self.name}


class Building(db.Model):
    __tablename__ = 'Building'
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(120))
    space = db.Column(db.Integer())
    floorscount = db.column(db.string(160))

    def json(self):
        return {"id": self.id, "address": self.address, "space": self.space, "floorscount": self.floorscount}
