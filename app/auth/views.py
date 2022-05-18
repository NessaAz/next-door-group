from . import auth_blueprint 
from flask import render_template,url_for,flash,redirect,request
from ..email import mail_message
from flask_login import login_user,login_required,logout_user
from .. import db
from ..models import User
from .forms import RegForm,LoginForm



@auth_blueprint.route('/signup')
def signup():
    return render_template('autho/signup.html')


@auth_blueprint.route('/login')
def login():
    return render_template('autho/login.html')


@auth_blueprint.route('/login', methods = ['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()
        if user != None and user.verify_password(form.password.data):
            login_user(user,form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('Invalid username or Password')
    return render_template('autho/login.html', loginform = form)

@auth_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))

@auth_blueprint.route('/signup', methods = ["GET","POST"])
def signup():
    form = RegForm()
    if form.validate_on_submit():
        user = User(email = form.email.data, username = form.username.data, password = form.password.data)
        user.save_u()
        
        return redirect(url_for('auth.login'))
    return render_template('autho/signup.html', r_form = form)

@auth_blueprint.route('/register',methods = ["GET","POST"])
def register():
    form = RegForm()
    if form.validate_on_submit():
        user = User(email = form.email.data, username = form.username.data,password = form.password.data)
        db.session.add(user)
        db.session.commit()

        mail_message("Welcome to next door","email/welcome_user",user.email,user=user)

        return redirect(url_for('auth.login'))
        title = "New Account"
    return render_template('autho/register.html',registration_form = form)