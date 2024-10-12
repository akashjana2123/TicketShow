from flask import Flask
from database import db
import os
from models import *


app=Flask(__name__)


app.config["SQLALCHEMY_DATABASE_URI"]=f"sqlite:///{os.path.abspath(os.path.dirname(__file__))}/database/ticket_show_application.db"

db.init_app(app)

@app.route('/')
def home():
    obj=Admin.query.first()
    return ( f"<h1>Hello {obj.admin_name}</h1>")

@app.route('/abc')
def abc():
    return 'Hello World'

if __name__ == '__main__':
    app.run(host='localhost', port=8000, debug=True)