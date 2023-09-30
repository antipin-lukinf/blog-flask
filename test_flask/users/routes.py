from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from test_flask import db, bcrypt
from test_flask.models import User, Post
from test_flask.users.forms import (RegistrationForm, LoginForm, UpdateAccountForm, RequestResetForm, ResetPasswordForm)

from test_flask.users.utils import save_picture

users = Blueprint('users', __name__)
