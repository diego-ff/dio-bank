from hmac import compare_digest as safe_str_cmp
from http import HTTPStatus

from flask import Blueprint, request
from flask_jwt_extended import JWTManager, create_access_token

from src.models import User, db

app = Blueprint("auth", __name__, url_prefix="/auth")


@app.route("/login", methods=["POST"])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    user = db.session.execute(db.select(User).where(User.username == username)).scalar()

    if  not user or user.password != password:
        return {"msg": "Bad username or password"}, HTTPStatus.UNAUTHORIZED

    access_token = create_access_token(identity=str(user.id))
    return {"access_token": access_token}

