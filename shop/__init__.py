from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class
import os

from flask_msearch import Search
from flask_login import LoginManager
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))
#Construction of the  the core app object...
app = Flask(__name__)
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

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
search = Search()
search.init_app(app)

migrate = Migrate(app, db)
with app.app_context():
    if db.engine.url.drivername == "sqlite":
        migrate.init_app(app, db, render_as_batch=True)
    else:
        migrate.init_app(app, db)

#Initializing flask_login  and this si the minimum that we need to set up a flask login 
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view='customerLogin'
login_manager.needs_refresh_message_category='danger'
login_manager.login_message = u"Please login first"


from shop.products import routes
from shop.admin import routes
from shop.carts import carts
from shop.customers import routes
