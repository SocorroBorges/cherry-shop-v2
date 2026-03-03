from flask import Blueprint, render_template

main = Blueprint("main", __name__)

@main.route("/")
def home():
    return "<h1>Cherry Shop v2 está viva</h1>"