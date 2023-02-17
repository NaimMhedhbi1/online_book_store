from flask import Flask #First, the Flask class was imported. This class will have our WSGI application as an instance.
from flask_sqlalchemy import SQLAlchemy ##create the SQLAlchemy object
from flask_bcrypt import Bcrypt #A Flask addon called Flask-Bcrypt gives your application access to bcrypt hashing tools.
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class #Your application can manage file uploading and providing the uploaded files flexibly and effectively using Flask-Upload
import os #It enables user interaction with the native OS that Python is currently running on when imported.
#Your application can manage file uploading and providing the uploaded files flexibly and effectively using Flask-Upload
from flask_msearch import Search
from flask_login import LoginManager
from flask_migrate import Migrate
#Python's flask-msearch module is frequently used in applications that leverage SQL databases and databases. Flask-msearch has a permissive license, a build file that is readily available, no bugs, no vulnerabilities, and little support. 

basedir = os.path.abspath(os.path.dirname(__file__))
#Construction of the  the core app object...
app = Flask(__name__)
#passing the special __name__ variable, which is needed for Flask to set up some paths behind the scenes.
## Configuration of the application 
# plugins initialization ; this is necessary. 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SECRET_KEY']='hfouewhfoiwefoquw'     #this is very important to be protected 
#losing this secret key means that the data of the customers can be risked and compromised. 
# in orderto encrypt all of users's passwords we use secret_key varaieble which  is a string. also to encrypt other sensitive informations
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Compile static assets
app.config['UPLOADED_PHOTOS_DEST'] = os.path.join(basedir, 'static/images')
photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)
patch_request_class(app)

database = SQLAlchemy(app) 
bcrypt = Bcrypt(app)
search = Search()
search.init_app(app)

migrate = Migrate(app, database)
#SQLite is a C-language library that implements a small, fast, self-contained, high-reliability, full-featured, SQL database engine.
with app.app_context():
    if database.engine.url.drivername == "sqlite": 
        migrate.init_app(app, database, render_as_batch=True)
    else:
        migrate.init_app(app, database)

#Initializing flask_login  and this si the minimum that we need to set up a flask login 
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view='customerLogin'
login_manager.needs_refresh_message_category='danger'
login_manager.login_message = u"Please login first"
#User session management is offered by Flask-Login for Flask. It manages routine operations like signing in and out and remembering your users' sessions for a long time.

from shop.products import routes
from shop.admin import routes
from shop.carts import carts
from shop.customers import routes
#the app.py file to create a Flask server with a single route

