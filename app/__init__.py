import os

from flask import Flask

from app.auth import login_required


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path, exist_ok=True)  # Updated to include exist_ok=True to prevent raising an error if the directory already exists
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/')
    @login_required
    def hello():
        return 'Hello, World!'

    #imports bps

    from . import auth

    #url
    app.register_blueprint(auth.bp)
    
    return app