from flask_wtf import FlaskForm
from wtforms import TextAreaField, EmailField, SearchField, StringField, SubmitField
from wtforms.validators import DataRequired, EqualTo


class AddHoodForm(FlaskForm):
    name = StringField('Hood Name', validators=[DataRequired()])
    about =TextAreaField('Tell us about your hood', validators=[DataRequired()])
    submit = SubmitField('Add Hood')