from flask import Blueprint

api = Blueprint('api', __name__)

from . import users, cars, gas_station, orders, peccancys
