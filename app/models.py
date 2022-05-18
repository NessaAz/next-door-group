from enum import unique
from . import db, login_manager
from flask_login import UserMixin, current_user
from werkzeug.security import generate_password_hash, check_password_hash


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(user_id)


class Users(UserMixin, db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String, unique=True, nullable=False)
  email = db.Column(db.String, unique=True, nullable=False)
  secure_password = db.Column(db.String, nullable=False)
  hoods = db.relationship('Hoods', backref='hoods', lazy=True)

  @property
  def password(self):
    raise AttributeError('You cannot read the password attribute')

  @password.setter
  def password(self, password):
    self.secure_password = generate_password_hash(password)

  def verify_password(self, password):
    return check_password_hash(self.secure_password, password)

  def __repr__(self):
    return f"User('{self.username}')"


class Hoods(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String, unique=True, nullable=False)
  about = db.Column(db.String, nullable=False)
  members = db.Column(db.Integer, default=1)# on button click update the memebers number
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'))  # admin
  amenities=db.relationship('Amenities', backref='amenities', lazy=True)


class Amenities(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  police_contact=db.Column(db.String)
  hospital_contact=db.Column(db.String)
  hood_id=db.Column(db.Integer, db.ForeignKey('hoods.id'))
