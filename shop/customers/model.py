from shop import database, login_manager
from datetime import datetime
from flask_login import UserMixin
import json

@login_manager.user_loader
def user_loader(user_id):
    return Register.query.get(user_id)

class Register(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key= True)
    username = database.Column(database.String(50), unique= True)
    name = database.Column(database.String(50), unique= False)
    password = database.Column(database.String(200), unique= False)
    email = database.Column(database.String(50), unique= True)
    contact = database.Column(database.String(50), unique= False)
    country = database.Column(database.String(50), unique= False)
    Street = database.Column(database.String(50), unique= False)
    city = database.Column(database.String(50), unique= False)
    date_created = database.Column(database.DateTime, nullable=False, default=datetime.utcnow)
    profile = database.Column(database.String(200), unique= False , default='profile.jpg')
    address = database.Column(database.String(50), unique= False)
    zipcode = database.Column(database.String(50), unique= False)
    TypeOfWork = database.Column(database.String(50), unique= False)
    employees =  database.Column(database.String(50), unique= False)
    Additional = database.Column(database.String(50), unique= False)
    place= database.Column(database.String(50), unique= False)
    code = database.Column(database.String(5), unique= False)
    phone= database.Column(database.String(5), unique= False)
    
    def __repr__(self):
        return '<Register %r>' % self.name


class JsonEcodedDict(database.TypeDecorator):
    impl = database.Text
    def process_bind_param(self, value, dialect):
        if value is None:
            return '{}'
        else:
            return json.dumps(value)
    def process_result_value(self, value, dialect):
        if value is None:
            return {}
        else:
            return json.loads(value)

class CustomerOrder(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    invoice = database.Column(database.String(20), unique=True, nullable=False)
    status = database.Column(database.String(20), default='Pending', nullable=False)
    customer_id = database.Column(database.Integer, unique=False, nullable=False)
    date_created = database.Column(database.DateTime, default=datetime.utcnow, nullable=False)
    orders = database.Column(JsonEcodedDict)

    def __repr__(self):
        return'<CustomerOrder %r>' % self.invoice



# Create Database Models
from shop import app 
app.app_context().push()
database.create_all()





