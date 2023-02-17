from flask import render_template,session, request,redirect,url_for,flash,current_app
from shop import db , app
from shop.products.models import Addproduct
from shop.products.routes import brands, categories
import json
#JSON (JavaScript Object Notation) is a lightweight data transfer format that was inspired by JavaScript object literal syntax. It is standardized by RFC 7159 (which replaces RFC 4627) and by ECMA-404 (although it is not a strict subset of JavaScript 1 ).
#Data values are kept as key:value pairs in dictionaries. A dictionary is a collection which is ordered*, changeable and do not allow duplicates.


def MagerDicts(dict1,dict2):
    if isinstance(dict1, list) and isinstance(dict2,list):
        return dict1  + dict2
    if isinstance(dict1, dict) and isinstance(dict2, dict):
        return dict(list(dict1.items()) + list(dict2.items()))
 #If the given object is an instance of the given type, the isinstance() function returns True; otherwise, it returns False.If the type parameter is a tuple, this function will return True if the object is one of the types in the tuple.
#We may import request and utilize request. args in Flask to obtain form request data. Request is used in the code above to retrieve the data contained

#Flask is informed by the #render template() function that the route should display an HTML template.
# app.route('/addcart') decorator to create a view function called Addcart().
@app.route('/addcart', methods=['POST'])
def AddCart():
    try:
        product_id = request.form.get('product_id')
        quantity = int(request.form.get('quantity'))
        color = request.form.get('colors')
        product = Addproduct.query.filter_by(id=product_id).first()

        if request.method =="POST":
            DictItems = {product_id:{'name':product.name,'price':float(product.price),'discount':product.discount,'color':color,'quantity':quantity,'image':product.image_1, 'colors':product.colors}}
            if 'Shoppingcart' in session:
                print(session['Shoppingcart'])
                if product_id in session['Shoppingcart']:
                    for key, item in session['Shoppingcart'].items():
                        if int(key) == int(product_id):
                            session.modified = True
                            item['quantity'] += 1
                else:
                    session['Shoppingcart'] = MagerDicts(session['Shoppingcart'], DictItems)
                    return redirect(request.referrer)
            else:
                session['Shoppingcart'] = DictItems
                return redirect(request.referrer)
              
    except Exception as e:
        print(e)
    finally:
        return redirect(request.referrer)
#The URL from which the request was made is contained in request.referrer, though the client may choose not to send it for a variety of reasons.
#The Session.query() method generates a query based on a given Session


#Flask is informed by the #render template() function that the route should display an HTML template.
# app.route('/carts') decorator to create a view function called getCart().
@app.route('/carts')
def getCart():
    if 'Shoppingcart' not in session or len(session['Shoppingcart']) <= 0:
        return redirect(url_for('home'))
    subtotal = 0
    grandtotal = 0
    for key,product in session['Shoppingcart'].items():
        discount = (product['discount']/100) * float(product['price'])
        subtotal += float(product['price']) * int(product['quantity'])
        subtotal -= discount
        tax =("%.2f" %(.06 * float(subtotal)))
        grandtotal = float("%.2f" % (1.06 * subtotal))
    return render_template('products/carts.html',tax=tax, grandtotal=grandtotal,brands=brands(),categories=categories())
#A view object is returned by the items() method. The dictionary's key-value pairs are present in the view object as tuples in a list.

#Flask is informed by the #render template() function that the route should display an HTML template.
# app.route('/updatecart/<int:code>') decorator to create a view function called updatecart().
@app.route('/updatecart/<int:code>', methods=['POST'])
def updatecart(code):
    if 'Shoppingcart' not in session or len(session['Shoppingcart']) <= 0:
        return redirect(url_for('home'))
    if request.method =="POST":
        quantity = request.form.get('quantity')
        color = request.form.get('color')
        try:
            session.modified = True
            for key , item in session['Shoppingcart'].items():
                if int(key) == code:
                    item['quantity'] = quantity
                    item['color'] = color
                    flash('Item is updated!')
                    return redirect(url_for('getCart'))
        except Exception as e:
            print(e)
            return redirect(url_for('getCart'))
#You can check a block of code for mistakes with the try block.
#Programs that handle particular exceptions can be written. Consider the example below, which prompts for input until a valid integer is entered, but allows the user to halt the application using Control-C or any other method that the operating system provides. Take note that a user-generated interruption is indicated by raising the KeyboardInterrupt exception.


#Flask is informed by the #render template() function that the route should display an HTML template.
# app.route('/deleteitem/<int:id>') decorator to create a view function called deleteitem().
@app.route('/deleteitem/<int:id>')
def deleteitem(id):
    if 'Shoppingcart' not in session or len(session['Shoppingcart']) <= 0:
        return redirect(url_for('home'))
    try:
        session.modified = True
        for key , item in session['Shoppingcart'].items():
            if int(key) == id:
                session['Shoppingcart'].pop(key, None)
                return redirect(url_for('getCart'))
    except Exception as e:
        print(e)
        return redirect(url_for('getCart'))


#Flask is informed by the #render template() function that the route should display an HTML template.
# app.route('/clearcart') decorator to create a view function called clearcart().
@app.route('/clearcart')
def clearcart():
    try:
        session.pop('Shoppingcart', None)
        return redirect(url_for('home'))
    except Exception as e:
        print(e)
