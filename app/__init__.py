import os
from flask import Flask
from flask_redis import FlaskRedis
from flask_cors import CORS

redis_client = FlaskRedis()

def create_app(test_config=None):
    print(f"running app with name: {__name__}")
    app = Flask(__name__, instance_relative_config=True, static_folder="../client/build", static_url_path="/")
    CORS(app)

    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    redis_client.init_app(app)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/')
    def index():
        return app.send_static_file('index.html')
    # @app.route('/')
    # def root():
    #     return 'serve index.html here'

    # from . import db
    # db.init_app(app)

    from . import api
    app.register_blueprint(api.bp)

    # from . import auth
    # app.register_blueprint(auth.bp)

    # from . import blog
    # app.register_blueprint(blog.bp)
    # app.add_url_rule('/', endpoint='index')


    return app