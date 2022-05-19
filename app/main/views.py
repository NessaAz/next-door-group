from . import main_blueprint
from flask import render_template, redirect, url_for, request
from flask_login import current_user
from .forms import AddHoodForm
from ..models import Hoods
from .. import db, photos
from werkzeug.utils import secure_filename
import uuid
import os

@main_blueprint.route('/')
def home():
    return render_template('index.html')

@main_blueprint.route('/add_hood', methods=['POST', 'GET'])
def addhood():
    form = AddHoodForm()
    if form.validate_on_submit():
        user_id = current_user._get_current_object().id
        file_name= form.hood_pic.data
        pic_file_name = secure_filename(file_name.filename)
        unique_pic_name=str(uuid.uuid1())+ '_'+ pic_file_name
        hood_pic = unique_pic_name
        hood = Hoods(name = form.name.data, about=form.about.data, hood_pic=hood_pic, user_id=user_id)

        db.session.add(hood)
        db.session.commit()
        
        filename = photos.save(form.hood_pic.data)
        path = f'images/{filename}'
        hood.hood_pic = path

        return redirect(url_for('main_blueprint.all_hoods', hood_pic = hood_pic))
    return render_template('add_hood.html', form=form)


@main_blueprint.route('/all_hoods')
def all_hoods():
    
    hoods = Hoods.query.all()
    return render_template('all_hoods.html', hoods=hoods)
