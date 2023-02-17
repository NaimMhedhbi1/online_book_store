from wtforms import BooleanField, StringField, PasswordField, validators , ValidationError
from flask_wtf import FlaskForm, Form
from .models import Visiter
#Secure Form : The FlaskForm will be a session secure form with csrf protection without any settings.
#User Sign-up Form
#With WTForms, validation is accomplished by assigning a field a collection of validators that will be executed when the containing form is validated. You give these using the second argument, validators, of the field constructor.
#<==================================================================================================>
class SignupForm(FlaskForm):
    name = StringField('Name', [validators.Length(min=4, max=25) , validators.DataRequired()]) 
    #   #wtforms.fields is a class. (Default Field Arguments)[source] StringFieldThis field, which represents an input type="text">, serves as the foundation for the majority of the more intricate fields.
    password = PasswordField('Password', [
        validators.Length(min=6, message='Try a stronger password'),
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Should be identical !')
    ])
    email = StringField('Email Address', [validators.Length(min=15, max=65),validators.Email(message='Enter a valid email'),validators.DataRequired()])
    #wtforms.fields is a class. (Default Field Arguments)[source] StringFieldThis field, which represents an input type="text">, serves as the foundation for the majority of the more intricate fields.
    username = StringField('Username', [validators.Length(min=4, max=25), validators.DataRequired()])
    #   #wtforms.fields is a class. (Default Field Arguments)[source] StringFieldThis field, which represents an input type="text">, serves as the foundation for the majority of the more intricate fields.
    #wtforms.fields is a class. Default Field Arguments for PasswordField[source] #Except that it creates an input type="password">, a StringField.
    confirm = PasswordField('Please check Your password again ! ')
    #wtforms.fields is a class. Default Field Arguments for PasswordField[source] #Except that it creates an input type="password">, a StringField.
    #How then do we retrieve data from our database? For this purpose Flask-SQLAlchemy provides a query attribute on your Model class. When you access it you will get back a new query object over all records. You can then use methods like filter() to filter the records before you fire the select with all() or first(). If you want to go by primary key you can also use get().   
    def check_username(self, field):
        if Visiter.query.filter_by(username=field.data).first():
            raise ValidationError('Try another one !already taken')   
    def check_email(self, field):
        if Visiter.query.filter_by(email=field.data).first():
            raise ValidationError('try another one! Already taken')         
#A validator merely accepts an input, checks to see if it satisfies some requirement, like a string's maximum length, and then returns. Otherwise it raises a ValidationError if the validation is unsuccessful. This method allows you to chain any number of field validators together and is really straightforward and adaptable.
#Servers and applications can both fail. You'll encounter an exception in production sooner or later. There will occasionally be exceptions even if your code is perfect. Why? Considering that all else will fall short. Here are some instances where flawless code can result in server issues.
#User Login Form 


class LoginForm(FlaskForm):
    password = PasswordField('New Password', [validators.DataRequired()])
    email = StringField('Email Address', [validators.Length(min=10, max=55),validators.DataRequired(),validators.Email(message='Enter a Valid Email')])
    

#Important Ideas
#WTForms' primary container is a form. Forms represent a group of fields that can be accessed using either the attribute style or form dictionary style.
#The bulk of the labor is performed by fields. Each field acts as a data type's representative and is responsible for converting form input to that data type. For instance, the data types represented by IntegerField and StringField are different. In addition to the data they hold, fields also have a number of helpful features like a label, description, and a list of validation errors.
#There is a Widget instance for each field. The widget's responsibility is to render an HTML version of that field. Each field can have a widget instance provided for it, although it makes sense for each field to have one by default. These fields are just for your convenience.
#There is a Widget instance for each field. The widget's responsibility is to render an HTML version of that field. Each field can have a widget instance provided for it, although it makes sense for each field to have one by default. Some fields are merely conveniences; for instance, a TextAreaField is just a StringField with a TextArea as the default widget.
#Fields provide a list of Validators that can be used to establish validation rules.