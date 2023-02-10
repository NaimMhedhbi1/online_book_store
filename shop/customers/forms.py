from wtforms import Form, StringField, TextAreaField, PasswordField,SubmitField,validators, ValidationError
from flask_wtf.file import FileRequired,FileAllowed, FileField
from flask_wtf import FlaskForm
from .model import Register




class CustomerRegisterForm(FlaskForm):
    name = StringField('name',[validators.Length(min=4, max=25) , validators.DataRequired()])
    username = StringField('username',[validators.DataRequired()])
    email = StringField('email', [validators.Length(min=15, max=65),validators.Email(message='Enter a valid email'),validators.DataRequired()])
    password = PasswordField('password', [
        validators.Length(min=6, message='Select a stronger password'),
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('confirm')
    country = StringField('country',[validators.DataRequired()])
    #city = StringField('City: ', [validators.DataRequired()])
    #contact = StringField('Contact: ', [validators.DataRequired()])
    #address = StringField('Address: ', [validators.DataRequired()])
    zipcode = StringField('zipcode',[validators.DataRequired()])
    TypeOfWork=StringField('TypeOfWork',[validators.DataRequired()])
    employees=StringField('employees',[validators.DataRequired()])
    Street = StringField('Street',[validators.DataRequired()])
    Additional = StringField('Additional',[validators.DataRequired()])
    place = StringField('place',[validators.DataRequired()])
    code = StringField('code',[validators.DataRequired()])
    phone = StringField('phone',[validators.DataRequired()])
    #profile = FileField(validators=[FileAllowed(['jpg','png','jpeg','gif'], 'Image only please')])
    submit = SubmitField('submit')

    def validate_username(self, username):
        if Register.query.filter_by(username=username.data).first():
            raise ValidationError("This username is already in use!")
        
    def validate_email(self, email):
        if Register.query.filter_by(email=email.data).first():
            raise ValidationError("This email address is already in use!")


class CustomerLoginFrom(FlaskForm):
    email = StringField('Email: ', [validators.Email(), validators.DataRequired()])
    password = PasswordField('Password: ', [validators.DataRequired()])

   




   

 

    

     

   


    

