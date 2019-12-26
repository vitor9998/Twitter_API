from flask import Blueprint, Response, request, jsonify
from .service import Tweets
import requests
import json



Lista = Blueprint(
    "user", __name__, url_prefix="/v1/tweet"
)



@Lista.route("/user/<nome>", methods=["GET"])
def Usuario(nome):
    a = Tweets.filtro(nome)
    b = json.dumps(a)    

    return b  
