from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, SelectField
from wtforms.fields.core import RadioField
from wtforms.fields.html5 import DateField, TimeField
from wtforms.validators import Required, Email, EqualTo
from ..models import User
from wtforms import ValidationError

from datetime import datetime


class RegistrationForm(FlaskForm):
    email = StringField('Your Email Address', validators=[
                        Required(), Email()], render_kw={'class': 'input-group'})
    username = StringField('Enter your username', validators=[
                           Required()], render_kw={'class': 'input-group'})
    password = PasswordField('Password', validators=[Required(), EqualTo(
        'password_confirm', message='Passwords must match')], render_kw={'class': 'input-group'})
    password_confirm = PasswordField(
        'Confirm Password', validators=[Required()])
    DOB = DateField('DOB', format='%Y-%m-%d',
                    default=datetime.now(), render_kw={'class': 'input-group'})
    MF = RadioField('Gender', choices=[
                    ('Male', 'Male'), ('Female', 'Female')], render_kw={'class': 'input-group'})
    submit = SubmitField('Sign Up', render_kw={'class': 'login-button'})

    def validate_email(self, data_field):
        if User.query.filter_by(email=data_field.data).first():
            raise ValidationError('There is an account with that email')

    def validate_username(self, data_field):
        if User.query.filter_by(username=data_field.data).first():
            raise ValidationError('That username is taken')


class LoginForm(FlaskForm):
    email = StringField('Your Email Address', validators=[
                        Required(), Email()], render_kw={'class': 'input-group'})
    password = PasswordField('Password', validators=[
                             Required()], render_kw={'class': 'input-group'})
    # remember = BooleanField('Remember me')
    submit = SubmitField('Sign In', render_kw={'class': 'login-button'})


class ReviewForm(FlaskForm):

    title = StringField('Review title', validators=[Required()])

    review = TextAreaField('Movie review')

    submit = SubmitField('Submit')
