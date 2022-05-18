from flask_wtf import FlaskForm
from wtforms import TextAreaField, StringField, SubmitField
from flask_wtf.file import FileField
from wtforms.validators import DataRequired


class AddHoodForm(FlaskForm):
    name = StringField('Hood Name', validators=[DataRequired()])
    about =TextAreaField('Tell us about your hood', validators=[DataRequired()])
    hood_pic = FileField('Photo of the hood', validators=[DataRequired()])
    submit = SubmitField('Add Hood')

class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')