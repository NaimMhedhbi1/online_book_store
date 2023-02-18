from wtforms import Form, StringField, TextAreaField, PasswordField,SubmitField,validators, ValidationError
from flask_wtf.file import FileRequired,FileAllowed, FileField
from flask_wtf import FlaskForm
from .model import Register
#The FileField offered by Flask-WTF is different from the field offered by WTForms. The data will be None if the file is an empty instance of FileStorage, which will be verified.

#wtforms.validators. DataRequired(message=None) verifies that the field's data is "truthy"; if not, the validation chain is terminated.
#This validator verifies that the field's data property has the value "true" (effectively, it does if field.data.) Moreover, a string that solely contains whitespace characters is regarded as false if the data is of the string type.

#<==================================================================================================>
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
    #wtforms.fields is a class. An input type="submit"> is represented by SubmitField(default field parameters). This enables determining whether a certain submit button has been pressed.
    def check_username(self, username):
        if Register.query.filter_by(username=username.data).first():
            raise ValidationError("This username is already in use!")
        
    def validate_email(self, email):
        if Register.query.filter_by(email=email.data).first():
            raise ValidationError("This email address is already in use!")
        
#wtforms.validators, please. Email(message=None, allow smtputf8=True, check deliverability=False, allow empty local=False, granular message=False)[source]
#checks an email address's validity. requires the installation of the email validator package. Pip install wtforms[email], for instance.

#Error message to raise for parameters in the event of a validation mistake.

#Utilize the validation failed message from the email validator library with granular messages (Default False).

#Check for domain name resolution with check deliverability (Default False).

#Allow addresses that would require SMTPUTF8 to fail validation (Default True).

#Accept an empty local portion (@example.com) when verifying Postfix aliases, for example (Default False).

class CustomerLoginFrom(FlaskForm):
    email = StringField('Email: ', [validators.Email(), validators.DataRequired()])
    password = PasswordField('Password: ', [validators.DataRequired()])






   

 

    

     

   


    

