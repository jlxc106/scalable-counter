import functools

from flask import ( 
    Blueprint, jsonify
    # , flash, g, redirect, render_template, request, session, url_for
)
from . import redis_client
# from werkzeug.security import check_password_hash, generate_password_hash

# from flaskr.db import get_db

bp = Blueprint('api', __name__, url_prefix='/api')

@bp.route('/item', methods=('GET', ))
def getItem():
    # return "some string"
    key = "count1"
    try:
        c = redis_client.get(key).decode('utf-8')
    except AttributeError:
        c = None
    print("count obj:", c)
    if c == None:
        redis_client.set(key, 1)
        c = 1
    else:
        c = int(c)+1
        redis_client.set(key, c)
    d = {"count": c}
    return jsonify(d)