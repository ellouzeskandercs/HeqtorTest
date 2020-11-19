from flask import request
from flask_restful import Resource
from flask_jwt_extended import get_jwt_identity, jwt_required

from heqtor.controllers import get_user


class Me(Resource):
    @jwt_required
    def get(self):
        user_id = get_jwt_identity()["id"]
        return get_user(user_id)

    @jwt_required
    def post(self):
        # TODO
        # hint : data from post request is located in flask object request.json
        pass


class MeCompany(Resource):
    # TODO
    # get, post, delete
    pass
