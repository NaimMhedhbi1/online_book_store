from wtforms import BooleanField, StringField, PasswordField, validators , ValidationError
from flask_wtf import FlaskForm, Form
from .models import User

#User Sign-up Form
class RegistrationForm(FlaskForm):
    name = StringField('Name', [validators.Length(min=4, max=25) , validators.DataRequired()])
    username = StringField('Username', [validators.Length(min=4, max=25), validators.DataRequired()])
    email = StringField('Email Address', [validators.Length(min=15, max=65),validators.Email(message='Enter a valid email'),validators.DataRequired()])
    password = PasswordField('Password', [
        validators.Length(min=6, message='Select a stronger password'),
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Confirm Your Password')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use.')

        
    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')
            

#User Login Form 
class LoginForm(FlaskForm):
    email = StringField('Email Address', [validators.Length(min=6, max=35),validators.DataRequired(),validators.Email(message='Enter a Valid Email')])
    password = PasswordField('New Password', [validators.DataRequired()])