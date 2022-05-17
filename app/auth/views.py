from . import auth_blueprint
from flask import render_template




@auth_blueprint.route('/signup')
def signup():
    return render_template('auth/signup.html')


@auth_blueprint.route('/login')
def login():
    return render_template('auth/login.html')
