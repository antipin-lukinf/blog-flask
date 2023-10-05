from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])       #заголовок поста
    content = TextAreaField('Content', validators=[DataRequired()]) # текст поста
    submit = SubmitField('Post')                                    # кнопка отправки
