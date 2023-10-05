from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from test_flask.config import Config
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
login_manager = LoginManager()

bcrypt = Bcrypt()


def create_app():
    print(__name__)
    app = Flask(__name__)
    bcrypt.init_app(app)

    db.init_app(app)
    login_manager.init_app(app)

    from test_flask.main.routes import main
    from test_flask.users.routes import users
    from test_flask.posts.routes import posts

    app.register_blueprint(main)  # регистрация blueprint из файла routes
    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.config.from_object(Config)
    return app



