from flask import Blueprint, render_template, request, redirect, url_for
from .models import Product
from . import db

main = Blueprint("main", __name__)

@main.route("/")
def home():
    products = Product.query.all()
    return render_template("home.html", products=products)

@main.route("/add-product", methods=["GET", "POST"])
def add_product():
    if request.method == "POST":
        name = request.form["name"]
        price = request.form["price"]
        description = request.form["description"]

        product = Product(
            name=name,
            price=float(price),
            description=description
        )

        db.session.add(product)
        db.session.commit()

        return redirect(url_for("main.home"))
    
    return render_template("add_product.html")