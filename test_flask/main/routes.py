from flask import render_template, Blueprint
from test_flask.models import User

main = Blueprint('main', __name__) #макет


@main.route("/")       #главная страница
@main.route("/home")       #страница home
def home():
    return render_template('home.html')
