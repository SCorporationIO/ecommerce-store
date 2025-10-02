from flask import Flask, render_template, redirect, url_for, request
from database.database import db
from database.models import Product, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/ecommerce.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'supersecretkey'

db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()
    # Add sample products if not exists
    if not Product.query.first():
        sample_products = [
            Product(name="Silk Saree", studio="Ruhé", price=120.0, image="saree1.jpg"),
            Product(name="Cotton Dress", studio="Élan Sutra", price=80.0, image="dress1.jpg"),
            Product(name="Handmade Kurta", studio="Kritá", price=100.0, image="kurta1.jpg"),
            Product(name="Chic Top", studio="Élan Sutra", price=60.0, image="dress1.jpg"),
            Product(name="Luxury Scarf", studio="Ruhé", price=50.0, image="saree1.jpg")
        ]
        db.session.add_all(sample_products)
        db.session.commit()

# Routes
@app.route('/')
def home():
    products = Product.query.all()
    return render_template('index.html', products=products)

@app.route('/studio')
def studio():
    return render_template('studio.html')

@app.route('/product/<int:product_id>')
def product_detail(product_id):
    product = Product.query.get_or_404(product_id)
    return render_template('product.html', product=product)

@app.route('/cart')
def cart():
    return render_template('cart.html')

@app.route('/checkout')
def checkout():
    return render_template('checkout.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/account')
def account():
    return render_template('account.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')
