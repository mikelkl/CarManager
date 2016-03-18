from app.api_1_0 import api
from app.models import MyPeccancy
from flask import jsonify


@api.route('/peccancy/<int:id>')
def get_peccancy(id):
    peccancy = MyPeccancy.query.get_or_404(id)
    return jsonify(peccancy.to_json())


@api.route('/peccancys')
def get_all_peccancy():
    peccancys = MyPeccancy.query.all()
    return jsonify({
        'peccancys': [peccancy.to_json() for peccancy in peccancys]
    })
