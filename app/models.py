# -*- coding: utf-8 -*-
import json
import urllib
from datetime import datetime
from urllib import urlencode

from app import db
from config import Config
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

    @staticmethod
    def generate_fake(count=100):
        from random import seed
        import forgery_py

        seed()
        for i in range(count):
            u = MyUser(phone_number="1234567890000098",
                       nick=forgery_py.internet.user_name(),
                       password=forgery_py.lorem_ipsum.word(),
                       sex=True,
                       member_since=forgery_py.date.date(True),
                       avatar=url_for('static', filename="1.png", _external=True),
                       age='20')
            db.session.add(u)
            try:
                db.session.commit()
            except:
                db.session.rollback()

    def to_json(self):
        return {
            "id": self.id,
            "phone_number": self.phone_number,
            "nick": self.nick,
            "sex": self.sex,
            "age": self.age,
            "member_since": self.member_since,
            "avatar": self.avatar,
            "cars": [car.to_json() for car in self.cars],
            "orders": [order.to_json() for order in self.orders]
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

    @staticmethod
    def generate_fake(count=100):
        from random import seed
        import forgery_py

        seed()
        for i in range(count):
            c = MyCar(license_plate_number=forgery_py.lorem_ipsum.word(),
                      brand=forgery_py.lorem_ipsum.word(),
                      car=forgery_py.lorem_ipsum.word(),
                      model=forgery_py.lorem_ipsum.word(),
                      engine_number=forgery_py.lorem_ipsum.word(),
                      milege=100,
                      remaining_oil=10,
                      engine_statu=True,
                      antomative_lighting_statu=True,
                      speed_changing_box_statu=True,
                      car_location=forgery_py.lorem_ipsum.word(),
                      registration_date=forgery_py.date.date(True),
                      img=forgery_py.lorem_ipsum.word(),
                      price=forgery_py.lorem_ipsum.word(),
                      displacement=forgery_py.lorem_ipsum.word(),
                      oil_consumption=forgery_py.lorem_ipsum.word(),
                      speed_changing_box=forgery_py.lorem_ipsum.word(),
                      car_type=forgery_py.lorem_ipsum.word(),
                      user_id=1
                      )
            db.session.add(c)
            try:
                db.session.commit()
            except:
                db.session.rollback()

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
                            _external=True),
            "peccancys": [peccancy.to_json() for peccancy in self.peccancys]
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

    @staticmethod
    def generate_fake(count=100):
        from random import seed
        import forgery_py

        seed()
        for i in range(count):
            o = MyRefuelOrder(order_time=forgery_py.date.date(True),
                              refuel_type=forgery_py.lorem_ipsum.word(),
                              refuel_amount=forgery_py.lorem_ipsum.word(),
                              user_id=1,
                              gas_station_id=1
                              )
            db.session.add(o)
            try:
                db.session.commit()
            except:
                db.session.rollback()

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

    @staticmethod
    def generate_fake(count=100):
        from random import seed
        import forgery_py

        seed()
        for i in range(count):
            p = MyPeccancy(peccancy_action=forgery_py.lorem_ipsum.word(),
                           peccancy_address=forgery_py.address.street_address(),
                           peccancy_time=forgery_py.date.date(True),
                           fine=1000,
                           deduct_point=10,
                           query_time=forgery_py.date.date(True),
                           car_id="nam"
                           )
            db.session.add(p)
            try:
                db.session.commit()
            except:
                db.session.rollback()

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

    # 检索周边加油站
    @staticmethod
    def request_data():
        url = "http://apis.juhe.cn/oil/local"
        params = {
            "lon": "103.909",  # 经纬(如:121.538123)
            "lat": "30.802",  # 纬度(如：31.677132)
            "r": "",  # 搜索范围，单位M，默认3000，最大10000
            "page": "1",  # 页数,默认1
            "format": "1",  # 格式选择1或2，默认1
            "key": Config.appkey,  # 应用APPKEY(应用详细页查询)
        }
        params = urlencode(params)
        f = urllib.urlopen("%s?%s" % (url, params))

        content = f.read()
        res = json.loads(content)
        if res:
            error_code = res["error_code"]
            if error_code == 0:
                # 成功请求
                # print res["result"]
                for station in res["result"]['data']:
                    # print station
                    s = MyGasStation()
                    s.name = station['name']
                    s.area = station['area']
                    s.areaname = station['areaname']
                    s.address = station['address']
                    s.brandname = station['brandname']
                    s.type = station['type']
                    s.discount = station['discount']
                    s.exhaust = station['exhaust']
                    s.position = station['position']
                    s.lon = station['lon']
                    s.lat = station['lat']
                    s.price = station['price']['E90']
                    if station['gastprice']:
                        s.gastprice = station['gastprice']['93#']
                    s.fwlsmc = station['fwlsmc']
                    db.session.add(s)
                db.session.commit()
            else:
                print "%s:%s" % (res["error_code"], res["reason"])
        else:
            print "request api error"

    @staticmethod
    def generate_fake(count=100):
        from random import seed
        import forgery_py

        seed()
        for i in range(count):
            s = MyGasStation(name=forgery_py.lorem_ipsum.word(),
                             area=forgery_py.lorem_ipsum.word(),
                             areaname=forgery_py.lorem_ipsum.word(),
                             address=forgery_py.lorem_ipsum.word(),
                             brandname=forgery_py.lorem_ipsum.word(),
                             type=forgery_py.lorem_ipsum.word(),
                             discount=forgery_py.lorem_ipsum.word(),
                             exhaust=forgery_py.lorem_ipsum.word(),
                             position=forgery_py.lorem_ipsum.word(),
                             price=forgery_py.lorem_ipsum.word(),
                             gastprice=forgery_py.lorem_ipsum.word(),
                             fwlsmc=forgery_py.lorem_ipsum.word(),
                             lat=100,
                             lon=100
                             )
            db.session.add(s)
            try:
                db.session.commit()
            except:
                db.session.rollback()

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "area": self.area,
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
            "lon": self.lon,
            "orders": [order.to_json() for order in self.orders]
        }

    def __repr__(self):
        print '<MyGasStation: %r>' % self.location
