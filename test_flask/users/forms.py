from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import *
from flask_login import current_user
from test_flask.models import User


class RegistrationForm(FlaskForm):
    username = StringField('Имя пользователя: ',
                           validators=[DataRequired(),
                                       Length(min=2, max=20)])
    email = StringField('Email:',
                        validators=[DataRequired(), Email()])

    password = PasswordField('Пароль', validators=[DataRequired()])

    confirm_password = PasswordField('Подтвердите пароль',
                                     validators=[DataRequired(),
                                                 EqualTo('password')])

    submit = SubmitField('Зарегистрироваться')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError(
                'Это имя занято'
            )

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError(
                'Этот email занят'
            )
