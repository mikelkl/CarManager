from app.api_1_0 import api
from app.models import MyUser
from flask import jsonify


@api.route('/user/<int:id>')
def get_user(id):
    user = MyUser.query.get_or_404(id)
    return jsonify(user.to_json())


@api.route('/users')
def get_all_user():
    users = MyUser.query.all()
    return jsonify({
        'users': [user.to_json() for user in users]
    })
