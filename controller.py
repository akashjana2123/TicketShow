from flask import current_app as app
from models import *

@app.route("/")
def home():
    obj=Admin.query.first()
    print(obj)

    return f'<h1 style="color:red"> this is your website\'s homepage{obj.admin_name}<h1><a href="/explore/home/national-capital-region-ncr">ncr page</a>'

@app.route("/explore/home/national-capital-region-ncr")
def ncr():
    return "NOt that movie"

@app.route("/explore/home/ahmedabad")
def ahmedabad():
    return "That local language movie"

@app.route("/abc")
def abc():

    return "This is ABC route's response"