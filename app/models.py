from datetime import datetime

from app import db
from werkzeug.security import generate_password_hash, check_password_hash


class MyUser(db.Model):
    __tablename__ = 'MyUser'

    id = db.Column(db.Integer, primary_key=True)
    phone_number = db.Column(db.String(20))
    password_hash = db.Column(db.String(128))
    nick = db.Column(db.String(64))
    sex = db.Column(db.Boolean)
    age = db.Column(db.String(5))
    member_since = db.Column(db.DateTime(), default=datetime.utcnow)
    avatar = db.Column(db.String(100))
    cars = db.relationship('MyCar', backref='owner', lazy='dynamic')
    orders = db.relationship('MyRefuelOrder', backref='creator', lazy='dynamic')

    @property
    def password(self):
        raise AttributeError('password is not a readble attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        print '<MyUser: %r>' % self.nick


class MyCar(db.Model):
    __tablename__ = 'MyCar'

    license_plate_number = db.Column(db.String(30), primary_key=True)
    brand = db.Column(db.String(20), index=True)
    car = db.Column(db.String(30), index=True)
    model = db.Column(db.String(30))
    engine_number = db.Column(db.String(30))
    milege = db.Column(db.Float)
    remaining_oil = db.Column(db.Float)
    engine_statu = db.Column(db.Boolean)
    antomative_lighting_statu = db.Column(db.Boolean)
    speed_changing_box_statu = db.Column(db.Boolean)
    car_location = db.Column(db.String(30))
    registration_date = db.Column(db.DateTime())
    img = db.Column(db.String(30))
    price = db.Column(db.String(30))
    displacement = db.Column(db.String(30))
    oil_consumption = db.Column(db.String(30))
    speed_changing_box = db.Column(db.String(30))
    car_type = db.Column(db.String(30))
    body_structure = db.Column(db.String(30))
    user_id = db.Column(db.Integer, db.ForeignKey('MyUser.id'))
    peccancys = db.relationship('MyPeccancy', backref='addPeccancy', lazy='dynamic')

    def __repr__(self):
        print '<MyCar: %r>' % self.license_plate_number


class MyRefuelOrder(db.Model):
    __tablename__ = 'MyRefuelOrder'

    id = db.Column(db.Integer, primary_key=True)
    order_time = db.Column(db.DateTime())
    refuel_type = db.Column(db.String(20))
    refuel_amount = db.Column(db.String(10))
    user_id = db.Column(db.Integer, db.ForeignKey('MyUser.id'))
    gas_station_id = db.Column(db.Integer, db.ForeignKey('MyGasStation.id'))

    def __repr__(self):
        print '<MyRefuelOrder: %r>' % self.order_time


class MyPeccancy(db.Model):
    __tablename__ = 'MyPeccancy'

    id = db.Column(db.Integer, primary_key=True)
    peccancy_action = db.Column(db.String(50))
    peccancy_address = db.Column(db.String(30))
    peccancy_time = db.Column(db.DateTime())
    fine = db.Column(db.Integer)
    deduct_point = db.Column(db.Integer)
    query_time = db.Column(db.DateTime())
    car_id = db.Column(db.Integer, db.ForeignKey('MyCar.license_plate_number'))

    def __repr__(self):
        print '<MyPeccancy: %r>' % self.peccancy_time


class MyGasStation(db.Model):
    __tablename__ = 'MyGasStation'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    area = db.Column(db.String(30))
    location = db.Column(db.String(30))
    areaname = db.Column(db.String(30))
    address = db.Column(db.String(30))
    brandname = db.Column(db.String(30))
    type = db.Column(db.String(30))
    discount = db.Column(db.String(30))
    exhaust = db.Column(db.String(30))
    position = db.Column(db.String(30))
    price = db.Column(db.String(30))
    gastprice = db.Column(db.String(30))
    fwlsmc = db.Column(db.String(30))
    lat = db.Column(db.Float)
    lon = db.Column(db.Float)

    def __repr__(self):
        print '<MyGasStation: %r>' % self.location
