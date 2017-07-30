from flask import render_template

from evac import app

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'world!'}  # fake user
    return render_template('index.html',
                           title='Home',
                           user=user)
