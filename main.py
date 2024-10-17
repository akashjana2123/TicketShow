from flask import Flask
import os
from database import db
from models import *


app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]=f"sqlite:///{os.path.abspath(os.path.dirname(__file__))}/database/ticket_show_application.db"

db.init_app(app)
app.app_context().push()

from  controllers.controllers import *

if __name__=="__main__":
    app.run(host="localhost", port=8080, debug=True)