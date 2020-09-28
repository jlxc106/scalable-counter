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
    db_c = 10
    
    #hincrby - hash increment by amount
#     #returns the updated value

#     X HINCRBY s12345:unique_visitors:daily 20140920 1    // returns the current hit count
#   SETNX   s12345:unique_visitors:sync 1              // succeeds because no sync has happened
#   SETEX   s12345:unique_visitors:sync 60 1           // makes the sync lock key expire
#   RENAME  s12345:unique_visitors:daily s12345:unique_visitors:daily_<RANDOM>  // isolates data for this sync
#   HSCAN   s12345:unique_visitors:daily_<RANDOM> ...  // repeat until we have all the data
#   * add results of hscan to MySQL *
#   DEL     s12345:unique_visitors:daily_<RANDOM>
    """
    upd_val = redis_client.hincrby("name", "key",  amount=1)
    if upd_val >49:
        print("trigger db sync")
    redis_client.setnx()
    redix_client.setex()
    """

    d = {"count": c + db_c}
    return jsonify(d)
    # return jsonify(d)
