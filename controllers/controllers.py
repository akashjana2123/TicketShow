from flask import current_app as app, render_template
from models import *
from controllers.user_controller import *
from controllers.admin_controller import *

@app.route("/")
def home():
    obj=Admin.query.first()
    print(obj)
    return render_template("index.html", admin_name=obj.admin_name)

@app.route("/explore/home/national-capital-region-ncr")
def ncr():
    return "NOt that movie"

@app.route("/explore/home/ahmedabad")
def ahmedabad():
    return "That local language movie"

@app.route("/abc")
def abc():

    return "This is ABC route's response"