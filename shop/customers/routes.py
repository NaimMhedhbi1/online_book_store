from flask import render_template,session, request,redirect,url_for,flash,current_app,make_response
from flask_login import login_required, current_user, logout_user, login_user
from shop import app,database,photos, search,bcrypt,login_manager
from .forms import CustomerRegisterForm, CustomerLoginFrom
from .model import Register,CustomerOrder
import secrets
import os #It enables user interaction with the native OS that Python is currently running on when imported.
import json
import pdfkit
import stripe

buplishable_key ='pk_test_MaILxTYQ15v5Uhd6NKI9wPdD00qdL0QZSl'
stripe.api_key ='sk_test_9JlhVB6qwjcRdYzizjdwgIo0Dt00N55uxbWy'
#Flask is informed by the #render template() function that the route should display an HTML template.
#Flask is informed by the #render template() function that the route should display an HTML template.
@app.route('/payment',methods=['POST']) # app.route('/payement') decorator to create a view function called payement()
def payment():
    invoice = request.get('invoice')
    amount = request.form.get('amount')
    customer = stripe.Customer.create(
      email=request.form['stripeEmail'],
      source=request.form['stripeToken'],
    )
    charge = stripe.Charge.create(
      customer=customer.id,
      description='Myshop',
      amount=amount,
      currency='usd',
    )
    orders =  CustomerOrder.query.filter_by(customer_id = current_user.id,invoice=invoice).order_by(CustomerOrder.id.desc()).first()
    orders.status = 'Paid'
    database.session.commit()
    return redirect(url_for('thanks'))
#Flask is informed by the #render template() function that the route should display an HTML template.
# app.route('/thanks') decorator to create a view function called thanks()
@app.route('/thanks')
def thanks():
    return render_template('customer/thank.html')

#Flask is informed by the #render template() function that the route should display an HTML template.
# app.route('/customr/register') decorator to create a view function called customer_register()
@app.route('/customer/register', methods=['GET','POST'])
def customer_register():
    form = CustomerRegisterForm()
    if form.validate_on_submit():
        hash_password = bcrypt.generate_password_hash(form.password.data)
        register = Register(name=form.name.data, username=form.username.data, email=form.email.data,password=hash_password,country=form.country.data,TypeOfWork=form.TypeOfWork.data,employees=form.employees.data,Street=form.Street.data,Additional=form.Additional.data,place=form.place.data,code=form.code.data,phone=form.phone.data, zipcode=form.zipcode.data)
        database.session.add(register)
        flash(f'Welcome {form.name.data} Thank you for registering', 'success')
        database.session.commit()
        return redirect(url_for('login'))

    return render_template('customer/register.html', form=form)

#Flask is informed by the #render template() function that the route should display an HTML template.
#should wait a little bit then you can login, should refined or solved!!!
#not instantly it logsin 
# app.route('/customer/login') decorator to create a view function called customerLogin()
@app.route('/customer/login', methods=['GET','POST'])
def customerLogin():
    form = CustomerLoginFrom()
    if form.validate_on_submit():
        user = Register.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            flash('You are login now!', 'success')
            next = request.args.get('next')
            return redirect(next or url_for('home'))
        flash('Incorrect email and password','danger')
        return redirect(url_for('customerLogin'))
            
    return render_template('customer/login.html', form=form)

#Flask is informed by the #render template() function that the route should display an HTML template.
@app.route('/customer/logout')
def customer_logout():
    logout_user()
    return redirect(url_for('home'))

def updateshoppingcart():
    for key, shopping in session['Shoppingcart'].items():
        session.modified = True
        del shopping['image']
        del shopping['colors']
    return updateshoppingcart
#Flask is informed by the #render template() function that the route should display an HTML template.
@app.route('/getorder')
@login_required
def get_order():
    if current_user.is_authenticated:
        customer_id = current_user.id
        invoice = secrets.token_hex(5)
        updateshoppingcart
        try:
            order = CustomerOrder(invoice=invoice,customer_id=customer_id,orders=session['Shoppingcart'])
            database.session.add(order)
            database.session.commit()
            session.pop('Shoppingcart')
            flash('Your order has been sent successfully','success')
            return redirect(url_for('orders',invoice=invoice))
        except Exception as e:
            print(e)
            flash('Some thing went wrong while get order', 'danger')
            return redirect(url_for('getCart'))
        
#Flask is informed by the #render template() function that the route should display an HTML template.
#Flask is informed by the #render template() function that the route should display an HTML template.
@app.route('/orders/<invoice>')
@login_required
def orders(invoice):
    if current_user.is_authenticated:
        grandTotal = 0
        subTotal = 0
        customer_id = current_user.id
        customer = Register.query.filter_by(id=customer_id).first()
        orders = CustomerOrder.query.filter_by(customer_id=customer_id, invoice=invoice).order_by(CustomerOrder.id.desc()).first()
        for _key, product in orders.orders.items():
            discount = (product['discount']/100) * float(product['price'])
            subTotal += float(product['price']) * int(product['quantity'])
            subTotal -= discount
            tax = ("%.2f" % (.06 * float(subTotal)))
            grandTotal = ("%.2f" % (1.06 * float(subTotal)))

    else:
        return redirect(url_for('customerLogin'))
    return render_template('customer/order.html', invoice=invoice, tax=tax,subTotal=subTotal,grandTotal=grandTotal,customer=customer,orders=orders)

#Flask is informed by the #render template() function that the route should display an HTML template.
#should save the library under this path in the local C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe
config = pdfkit.configuration(wkhtmltopdf='C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')
@app.route('/get_pdf/<invoice>', methods=['POST'])
@login_required
def get_pdf(invoice):
    if current_user.is_authenticated:
        grandTotal = 0
        subTotal = 0
        customer_id = current_user.id
        if request.method =="POST":
            customer = Register.query.filter_by(id=customer_id).first()
            orders = CustomerOrder.query.filter_by(customer_id=customer_id, invoice=invoice).order_by(CustomerOrder.id.desc()).first()
            for _key, product in orders.orders.items():
                discount = (product['discount']/100) * float(product['price'])
                subTotal += float(product['price']) * int(product['quantity'])
                subTotal -= discount
                tax = ("%.2f" % (.06 * float(subTotal)))
                grandTotal = float("%.2f" % (1.06 * subTotal))

            rendered =  render_template('customer/pdf.html', invoice=invoice, tax=tax,grandTotal=grandTotal,customer=customer,orders=orders)
            pdf = pdfkit.from_string(rendered, False,configuration = config)
            response = make_response(pdf)
            response.headers['content-Type'] ='application/pdf'
            response.headers['content-Disposition'] ='inline; filename='+invoice+'.pdf'
            return response
    return request(url_for('orders'))

#Flask is informed by the #render template() function that the route should display an HTML template.


