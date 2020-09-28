import functools
from time import time
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
    start = time()
    # return "some string"
    key = "count1"
    try:
        c = redis_client.get(key).decode('utf-8')
    except AttributeError:
        c = None
    # print("count obj:", c)
    if c == None:
        redis_client.set(key, 1)
        c = 1
    else:
        c = int(c)
        redis_client.set(key, c+1)
    d = {"count": c}
    end = time()
    print(f"{end - start} seconds to run /api/item")
    return jsonify(d)