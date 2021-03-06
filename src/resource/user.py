from flask.ext.restful import Resource

from model.user import db, User
from util import parse_params


class UserListAPI(Resource):
    def get(self):
        return {'data': [user.json for user in User.query]}

    @parse_params(
        {'name': 'email', 'type': str, 'required': True},
        {'name': 'password', 'type': str, 'required': True}
    )
    def post(self, params):
        user = User(**params)
        db.session.add(user)
        db.session.commit()
        return user.json


class UserAPI(Resource):
    def get(self, id):
        user = User.query.get(id)
        return user.json
