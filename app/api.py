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