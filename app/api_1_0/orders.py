from app.api_1_0 import api
from app.models import MyRefuelOrder
from flask import jsonify


@api.route('/order/<int:id>')
def get_order(id):
    order = MyRefuelOrder.query.get_or_404(id)
    return jsonify(order.to_json())


@api.route('/orders')
def get_all_order():
    orders = MyRefuelOrder.query.all()
    return jsonify({
        'orders': [order.to_json() for order in orders]
    })
