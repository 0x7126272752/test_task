from typing import cast
from flask import request
from flask.views import MethodView

from marshmallow import Schema, fields
from core.users import forgot_password, change_password

from ..shared.utils import (
    success_response,
    error_reponse,
)


class ForgotPassword(MethodView):
    class PostSchema(Schema):
        username = fields.Str(required=True)

    class ChangePasswordSchema(Schema):
        password = fields.Str(required=True)
        confirmPassword = fields.Str(required=True)
        token = fields.Str(required=True)

    def post(self):
        try:
            if not request.is_json:
                raise Exception("Request is not JSON")

            json_data = request.data.decode("utf-8")
            schema = ForgotPassword.PostSchema()
            data = cast(dict[str, str], schema.loads(json_data))
            token = forgot_password(data["username"])

            response = success_response(data={"token": token})

            return response

        except Exception as e:
            return error_reponse(e)

    def put(self):
        try:
            if not request.is_json:
                raise Exception("Request is not JSON")

            json_data = request.data.decode("utf-8")
            schema = ForgotPassword.ChangePasswordSchema()
            data = cast(dict[str, str], schema.loads(json_data))
            change_password(data)

            response = success_response(data={"status": "ok"})

            return response

        except Exception as e:
            return error_reponse(e)
