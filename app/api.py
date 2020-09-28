import functools
from time import time
from flask import (
    Blueprint, jsonify, request
    # , flash, g, redirect, render_template, request, session, url_for
)
from . import redis_client
# from werkzeug.security import check_password_hash, generate_password_hash

# from flaskr.db import get_db

bp = Blueprint('api', __name__, url_prefix='/api')

@bp.route('/item', methods=('GET', ))
def getItem():
    ci_headerKey = "counter-increment"
    ci_headerVal = request.headers.get(ci_headerKey)
    # print("counter-increment value: ", ci_headerVal)
    start = time()
    key = "count1"
    try:
        c = int(redis_client.get(key).decode('utf-8'))
    except AttributeError:
        c = 0

    if int(ci_headerVal) == 1:
        c += 1
    redis_client.set(key, c)
    d = {"count": c}
    end = time()
    print(f"{end - start} seconds to run /api/item")
    return jsonify(d)
