from crypt import methods
from . import main_blueprint
from flask import render_template, redirect, url_for
from flask_login import current_user
from .forms import AddHoodForm
from ..models import Hoods
from .. import db



@main_blueprint.route('/')
def home():
    return render_template('index.html')



@main_blueprint.route('/add_hood', methods=['POST', 'GET'])
def addhood():
    form = AddHoodForm()
    if form.validate_on_submit():
        user_id = current_user._get_current_object().id
        hood = Hoods(name = form.name.data, about=form.about.data, user_id=user_id)
        db.session.add(hood)
        db.session.commit()
        return redirect(url_for('main_blueprint.all_hoods'))
    return render_template('add_hood.html', form=form)


@main_blueprint.route('/all_hoods')
def all_hoods():
    return render_template('all_hoods.html')
