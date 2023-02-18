from wtforms import Form, SubmitField,IntegerField,FloatField,StringField,TextAreaField,validators
from flask_wtf.file import FileField,FileRequired,FileAllowed

class Addproducts(Form):
    name = StringField('Name', [validators.DataRequired()])
    #wtforms.fields is a class. IntegerField(default field parameters) (default field arguments)
    price = FloatField('Price', [validators.DataRequired()])
    discount = IntegerField('Discount', default=0)
    stock = IntegerField('Stock', [validators.DataRequired()])
    colors = StringField('Colors', [validators.DataRequired()])
    discription = TextAreaField('Discription', [validators.DataRequired()])
    #A text field with the exception that all input must be an integer. Incorrect input is disregarded and won't be taken as a value.
    #The FileField offered by Flask-WTF is different from the field offered by WTForms. The data will be None if the file is an empty instance of FileStorage, which will be verified.wtforms.validators. Length(max=1, min=1, message=None)[source].verifies a string's length.
    image_1 = FileField('Image 1', validators=[FileRequired(), FileAllowed(['jpg','png','gif','jpeg'])])
    image_2 = FileField('Image 2', validators=[FileRequired(), FileAllowed(['jpg','png','gif','jpeg'])])
    image_3 = FileField('Image 3', validators=[FileRequired(), FileAllowed(['jpg','png','gif','jpeg'])])
    
"""
The string's minimum necessary length is specified by the parameter min. The minimum length won't be verified if it's not specified.

max - The string's maximum length. The maximum length won't be verified if it's not specified.

message - The error message to display in the event of a validation mistake. can be interpolated if needed using %(min)d and %(max)d. Depending on the presence of min and max, useful defaults are offered.        
"""
######## Flask
from flask_wtf import FlaskForm
class Review_form(FlaskForm):
    review = TextAreaField('reviews',
                                [validators.DataRequired(),
                                validators.length(min=1)])
    submit = SubmitField('submit')
