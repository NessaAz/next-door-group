from . import auth_blueprint , autho
from flask import render_template,url_for,flash,redirect,request
#from ..email import mail_message
from flask_login import login_user,login_required,logout_user
from .forms import RegForm,LoginForm
from ..models import User
from .. import db



@auth_blueprint.route('/signup')
def signup():
    return render_template('autho/signup.html')


@auth_blueprint.route('/login')
def login():
    return render_template('autho/login.html')


@autho.route('/login', methods = ['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()
        if user != None and user.verify_password(form.password.data):
            login_user(user,form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('Invalid username or Password')
    return render_template('autho/login.html', loginform = form)

@autho.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))

@autho.route('/signup', methods = ["GET","POST"])
def signup():
    form = RegForm()
    if form.validate_on_submit():
        user = User(email = form.email.data, username = form.username.data, password = form.password.data)
        user.save_u()
        
        return redirect(url_for('auth.login'))
    return render_template('autho/signup.html', r_form = form)