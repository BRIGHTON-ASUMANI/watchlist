from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField, DateField, ValidationError
from wtforms.fields.core import RadioField
from wtforms.validators import Required, Email
from ..models import User


class ReviewForm(FlaskForm):
    title = StringField('Review title', validators=[Required()])
    review = TextAreaField('Movie review')
    submit = SubmitField('Submit')


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.', validators=[Required()])
    DOB = DateField('DOB', format='%Y-%m-%d')
    MF = RadioField('Gender', choices=[('M', 'Male'), ('F', 'Female')])
    submit = SubmitField('Submit')
