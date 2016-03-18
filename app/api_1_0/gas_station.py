from app.api_1_0 import api
from app.models import MyGasStation
from flask import jsonify


@api.route('/gas_station/<int:id>')
def get_gas_station(id):
    gas_station = MyGasStation.query.get_or_404(id)
    return jsonify(gas_station.to_json())


@api.route('/gas_stations')
def get_all_gas_station():
    gas_stations = MyGasStation.query.all()
    return jsonify({
        'gas_stations': [gas_station.to_json() for gas_station in gas_stations]
    })
