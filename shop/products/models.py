from shop import db
from datetime import datetime


class Addproduct(db.Model):
    __seachbale__ = ['name','desc']
    id = db.Column(db.Integer, primary_key=True)
    #To define a column, use Column. The name you provide the column serves as its name. A string with the desired column name is an optional first argument that you can use to specify a different name for the column in the table. primary key=True designates a primary key. A compound primary key is created when many keys are designated as primary keys.
    #Each record in a table is given a special identification by the PRIMARY KEY constraint. Primary keys cannot have NULL values and must have UNIQUE values.
    name = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Numeric(10,2), nullable=False)
    discount = db.Column(db.Integer, default=0)
    stock = db.Column(db.Integer, nullable=False)
    colors = db.Column(db.Text, nullable=False)
    desc = db.Column(db.Text, nullable=False)
    pub_date = db.Column(db.DateTime, nullable=False,default=datetime.utcnow)
    #The names of the basic types, like String, Numeric, Integer, and DateTime, are in "CamelCase." TypeEngine's immediate subclasses are all "CamelCase" types. The "CamelCase" types are as database agnostic as feasible, which means they may all be used on any database backend and achieve the correct behavior by acting in a manner that is appropriate to that backend.
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'),nullable=False)
    category = db.relationship('Category',backref=db.backref('categories', lazy=True))
    #The names of the basic types, like String, Numeric, Integer, and DateTime, are in "CamelCase." TypeEngine's immediate subclasses are all "CamelCase" types. The "CamelCase" types are as database agnostic as feasible, which means they may all be used on any database backend and achieve the correct behavior by acting in a manner that is appropriate to that backend.
    brand_id = db.Column(db.Integer, db.ForeignKey('brand.id'),nullable=False)
    #A field (or group of fields) in one table that refers to the PRIMARY KEY in another table is known as a FOREIGN KEY.The table with the main key is referred to as the parent table, while the table with the foreign key is referred to as the child table.
    brand = db.relationship('Brand',backref=db.backref('brands', lazy=True))
    #The relationship() construct's relationship.backref keyword argument enables the automated creation of a new relationship() that will be added to the ORM mapping for the associated class. Then, with both relationship() constructions referencing the original relationship() construct, it will be added to a relationship.back populates configuration.
    image_1 = db.Column(db.String(150), nullable=False, default='image1.jpg')
    image_2 = db.Column(db.String(150), nullable=False, default='image2.jpg')
    image_3 = db.Column(db.String(150), nullable=False, default='image3.jpg')

    def __repr__(self):
        return '<Post %r>' % self.name


class Brand(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)

    def __repr__(self):
        return '<Brand %r>' % self.name
    

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)

    def __repr__(self):
        return '<Catgory %r>' % self.name

from shop import app 
app.app_context().push() 
db.create_all()
#Simply import the db object from an interactive Python shell and use the SQLAlchemy.create all() method to build the basic database, creating the tables and database
#Throughout a request, CLI command, or other action, the application context keeps track of the application-level data.
#Upon processing a request, Flask automatically pushes an application context.