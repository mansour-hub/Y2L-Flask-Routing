from flask import Flask, request, redirect, url_for, render_template
from flask import session as login_session

from databases import *
app = Flask(__name__)
app.secret_key = "MY_SUPER_SECRET_KEY"

@app.route('/')
def hey():
	return render_template("home1.html")

@app.route('/store')
def hello():
	products=session.query(products).all()
	return render_template("store.html", products = products)

@app.route('/cart')
def hii():
	return render_template("cart.html")

@app.route('/about')
def heyz():
	return render_template("about.html")

@app.route('/store/<string:name>')
def hello_name_route(name):
    return render_template(
        'store.html', n = name)

if __name__ == '__main__':
    app.run(debug=True)