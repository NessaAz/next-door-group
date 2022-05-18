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

  @property
  def password(self):
    raise AttributeError('You cannot read the password attribute')

  @password.setter
  def password(self, password):
    self.secure_password = generate_password_hash(password)

  def verify_password(self,password):
    return check_password_hash(self.secure_password,password)

  def __repr__(self):
    return f"User('{self.username}')"