from flask import Flask, render_template
from app import app
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