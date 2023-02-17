from flask import render_template,session, request,redirect,url_for,flash
from shop import app,database,bcrypt
from .forms import SignupForm,LoginForm
from .models import Admin_Admin
from shop.products.models import Addproduct,Category,Brand
#Flask-Session is an extension for Flask that adds support for Server-side Session to your application.
#The URL rule is prefixed with the blueprint’s URL prefix. The endpoint name, used with url_for(), is prefixed with the blueprint’s name.
#Flask is informed by the #render template() function that the route should display an HTML template.
#<==================================================================================================>


# app.route('/admin') decorator to create a view function called admin().
@app.route('/admin')
def admin():
    products = Addproduct.query.all()
    return render_template('admin/index.html', title='Admin page',products=products)


# app.route('/terms') decorator to create a view function called terms().
@app.route('/terms',methods=['GET','POST'])
def terms():
    return render_template('admin/terms.html')

#Flask is informed by the #render template() function that the route should display an HTML template.
# app.route('/blog') decorator to create a view function called blog().
@app.route('/blog',methods=['GET','POST'])
def blog():
    return render_template('admin/blog.html')


# app.route('/brands') decorator to create a view function called brands()
@app.route('/brands')
def brands():
    brands = Brand.query.order_by(Brand.id.desc()).all()
    return render_template('admin/brand.html', title='brands',brands=brands)


# app.route('/categories') decorator to create a view function called categories()
@app.route('/categories')
def categories():
    categories = Category.query.order_by(Category.id.desc()).all()
    return render_template('admin/brand.html', title='categories',categories=categories)


#Flask is informed by the #render template() function that the route should display an HTML template.
# app.route('/register') decorator to create a view function called register()
@app.route('/register', methods=['GET', 'POST']) 
def register():
    form = SignupForm()
    if form.validate_on_submit():
        hash_password = bcrypt.generate_password_hash(form.password.data) #Create hashed password. 
        user = Admin_Admin(name=form.name.data,username=form.username.data, email=form.email.data,
                    password=hash_password)
        database.session.add(user)
        flash(f'Welcome {form.name.data} Thanks for registering','success')
        database.session.commit()
        return redirect(url_for('login'))
    return render_template('admin/register.html',title='Register user', form=form)


#Flask is informed by the #render template() function that the route should display an HTML template.
# app.route('/login') decorator to create a view function called login()
#<==================================================================================================>
@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = Admin_Admin.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            session['email'] = form.email.data
            flash(f'Welcome {form.email.data} You are Logedin now','success')
            return redirect(url_for('admin'))
        else:
            flash(f'Wrong Email Or Password', 'danger')
            return redirect(url_for('login'))
    return render_template('admin/login.html',title='Login page',form=form) 
#<==================================================================================================>
#Flask is informed by the #render template() function that the route should display an HTML template.
#If it is a POST request, #validate on submit will determine whether it is valid.
#Based on the supplied value, the first() method returns the first n rows. To make this technique function as intended, the index must contain dates.
#Verify a password against the hashed and salted value provided. This function accepts plain text passwords, md5 hashes, and sha1 hashes in order to enable unsalted legacy passwords (both salted and unsalted).
#With the flashing system in Flask, users can receive feedback in a really straightforward manner. Using the flashing system, a message can essentially be recorded at the conclusion of a request and accessed only on the subsequent request. Usually, a layout template that accomplishes this is combined with this.