from shop import database
from datetime import datetime
#<==================================================================================================>
#Classes for manipulating dates and times are available in the datetime module.Although date and time calculations are enabled, the implementation's main goal is to efficiently extract attribute data for output formatting and manipulation.
"""
Models which inherit UserMixin immediately gain access to 4 useful methods:
1- is_authenticated: Checks to see if the current user is already authenticated, thus allowing them to bypass login screens.
2- is_active: If your app supports disabling or temporarily banning accounts, we can check if user.is_active() to handle a case where their account exists, but have been banished from the land.
3- is_anonymous: Many apps have a case where user accounts aren't entirely black-and-white, and anonymous users have access to interact without authenticating. This method might come in handy for allowing anonymous blog comments (which is madness, by the way).
4- get_id: Fetches a unique ID identifying the user.

What does Flask's database Model mean?
A Model is a Python class that represents a database table, and each of its characteristics corresponds to a table column. A model class inherits from database.Model and defines columns as an instance of database.Column class.
"""
#<==================================================================================================>
class db_posts(database.Model):   
    id =database.Column(database.Integer,primary_key=True)
    username=database.Column(database.String)
    title=database.Column(database.String)
    link=database.Column(database.String)
    content=database.Column(database.String)
    def __init__(self,username,title,link,content):
        self.username=username
        self.title=title
        self.link=link
        self.content = content

class Admin_Admin(database.Model):
    id = database.Column(database.Integer, primary_key=True) #should be unique 
    name = database.Column(database.String(60),unique=False, nullable=False) #unique is equal to false, two users can have the same name but noit the same user name  
    username = database.Column(database.String(100), unique=True, nullable=False) 
    email = database.Column(database.String(100), unique=True, nullable=False) #should be a valid email otherwise it will be refused. 
    password = database.Column(database.String(50),unique=False, nullable=False) #the database will store hashed passwords. even if the length of the password is 9 characters for example, in our database will be in a differen lenght and looking. this is because of the hashing operation 
    profile = database.Column(database.String(140), unique=False, nullable=False,default='profile.jpg')

    def __repr__(self):
        return '<Admin_Admin %r>' % self.username
#<==================================================================================================>
#The repr method is used to get a string representation of a Python object. It is common to find people using it when creating models for their flask app.
#With the repr method, you can make a query from the database and print the result of the query. Instead of getting the location of the query object in memory, the repr method provides a better representation of the result.
# store users preparing our database
#create and validate the user 
#create a user model 
#managing users require a boilerplate methods athat are necesary in such work. 
#<==================================================================================================>
from shop import app 
app.app_context().push()
database.create_all()

