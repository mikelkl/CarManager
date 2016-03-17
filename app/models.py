from datetime import datetime

from app import db
from flask import url_for
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

    def to_json(self):
        return {
            "id": self.id,
            "phone_number": self.phone_number,
            "nick": self.nick,
            "sex": self.sex,
            "age": self.age,
            "member_since": self.member_since,
            "avatar": self.avatar
        }

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

    def to_json(self):
        return {
            "license_plate_number": self.license_plate_number,
            "brand": self.brand,
            "car": self.car,
            "model": self.model,
            "engine_number": self.engine_number,
            "milege": self.milege,
            "remaining_oil": self.remaining_oil,
            "engine_statu": self.engine_statu,
            "antomative_lighting_statu": self.antomative_lighting_statu,
            "speed_changing_box_statu": self.speed_changing_box_statu,
            "car_location": self.car_location,
            "registration_date": self.registration_date,
            "img": self.img,
            "price": self.price,
            "displacement": self.displacement,
            "oil_consumption": self.oil_consumption,
            "speed_changing_box": self.speed_changing_box,
            "car_type": self.car_type,
            "body_structure": self.body_structure,
            'user': url_for('api.get_user', id=self.user_id,
                            _external=True)
        }

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

    def to_json(self):
        return {
            "id": self.id,
            "order_time": self.order_time,
            "refuel_type": self.refuel_type,
            "refuel_amount": self.refuel_amount,
            'user': url_for('api.get_user', id=self.user_id,
                            _external=True),
            'gas_station': url_for('api.get_gas_station', id=self.gas_station_id,
                                   _external=True)
        }

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
    car_id = db.Column(db.String(30), db.ForeignKey('MyCar.license_plate_number'))

    def to_json(self):
        return {
            "id": self.id,
            "peccancy_action": self.peccancy_action,
            "peccancy_address": self.peccancy_address,
            "peccancy_time": self.peccancy_time,
            "fine": self.fine,
            "deduct_point": self.deduct_point,
            "query_time": self.query_time,
            'car': url_for('api.get_car', id=self.car_id,
                           _external=True)
        }

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
    orders = db.relationship('MyRefuelOrder', backref='with', lazy='dynamic')

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "area": self.area,
            "location": self.location,
            "areaname": self.areaname,
            "address": self.address,
            "brandname": self.brandname,
            "type": self.type,
            "discount": self.discount,
            "exhaust": self.exhaust,
            "position": self.position,
            "price": self.price,
            "gastprice": self.gastprice,
            "fwlsmc": self.fwlsmc,
            "lat": self.lat,
            "lon": self.lon
        }

    def __repr__(self):
        print '<MyGasStation: %r>' % self.location
