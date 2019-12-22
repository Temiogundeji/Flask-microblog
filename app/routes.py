from flask import Flask, render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm
@app.route('/')
@app.route('/index')
def index():
    user= {'username':'Yusuff'}
    posts = [
        {
        'author':{'username': 'Yusuff'},
        'body':'I am Yusuff, a Full stack developer'
        },
        {
        'author':{'username': 'Isiak'},
        'body':'I am Isiak, a Chemical Engineer'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)