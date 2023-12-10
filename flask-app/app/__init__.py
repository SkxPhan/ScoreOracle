import os

from app import db
from app.views import auth
from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="dev",  # nosec
        DATABASE=os.path.join(app.instance_path, "ScoreOracle.sqlite"),
    )

    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # test page
    @app.route("/hello")
    def hello():
        return "Hello, World!"

    db.init_app(app)

    app.register_blueprint(auth.bp)

    return app
