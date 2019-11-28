from model import *


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_product(name, price, picture_link, description):

    product_object = Product(
        name=name,
        price=price,
        picture_link=picture_link,
        description=description)
    session.add(product_object)
    session.commit()


add_product("iphone", 3000 , "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQlJD8T1EZgy4-_qD2o4uXbQlm81K9SxyY0NvJEoPrKqHN3wqIU&s" , "iphone x")

def delete_product(the_name):
	
	session.query().filter_by(
		name=the_name).first().delete()
	session.commit()

def update_product(name, price, picture_link, description):

	Product = session.query(Product).filter_by(
		name=name).first()
	Product.name = name
	Product.price = price
	Product.picture_link = picture_link
	Product.description = description

	session.commit()

def query_all():

	Product = session.query(
		Product).all()
	return Product

def query_by_name(the_name):

	Product1 = session.query(
		Product).filter_by(
		name=the_name).first()
	return Product1

def add_to_cart(ProductID):

    productID_object = cart(
        ProductID=ProductID)
    session.add(productID_object)
    session.commit()

# add_product("Name", 100, "https://bit.ly/2KGDzhF", "Some things")
# products = query_all()