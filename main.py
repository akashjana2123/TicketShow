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
    return (
        "<h1>Welcome to my Flask App!</h1>"
        "<p>This is a simple Flask application.</p>"
        "<p>To view this page, navigate to <a href='http://localhost:8000'>http://localhost:8000</a></p>"
        "<p>Please note that this is a static website and does not have any dynamic content.</p>"
        f"here is the database for you: {obj}"
    )

if __name__ == '__main__':
    app.run(host='localhost', port=8000, debug=True)