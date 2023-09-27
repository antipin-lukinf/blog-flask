from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from test_flask.config import Config

db = SQLAlchemy()
login_manager = LoginManager()


def create_app():
    print(__name__)
    app = Flask(__name__)

    db.init_app(app)
    login_manager.init_app(app)

    from test_flask.main.routes import main
    app.register_blueprint(main)       #регистрация blueprint из файла routes
    app.config.from_object(Config)
    return app
