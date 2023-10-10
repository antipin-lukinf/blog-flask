from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from test_flask import db
from test_flask.models import Post
from test_flask.posts.forms import PostForm

posts = Blueprint('posts', __name__)


@posts.route("/allpost")
@login_required
def allpost():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()). \
        paginate(page=page, per_page=5)
    return render_template('allpost.html', posts=posts)


@posts.route("/post/new", methods=['GET', 'POST'])  # создание нового поста
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data,
                    author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Ваш пост создан!', 'success')
        return redirect(url_for('posts.allpost'))
    return render_template('create_post.html',
                           title='Новый пост', form=form, legend='Новый пост')


@posts.route("/post/<int:post_id>")
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post)
