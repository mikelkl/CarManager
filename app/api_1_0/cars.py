from app.api_1_0 import api
from app.models import MyCar
from flask import jsonify


@api.route('/car/<id>')
def get_car(id):
    car = MyCar.query.get_or_404(id)
    return jsonify(car.to_json())


@api.route('/cars')
def get_all_car():
    cars = MyCar.query.all()
    return jsonify({
        'cars': [car.to_json() for car in cars]
    })
