from flask import current_app as app, render_template, request
from models import *


@app.route("/user_login", methods=["GET", "POST"])
def user_login():
    if request.method=="POST":
        user_name=request.form.get("user_name")
        user_obj=User.query.get(user_name)
        password=request.form.get("user_password")
        print(f"user_name received:{user_name}, user password from form:{password}")
        if user_obj:
            # user name matched
            if user_obj.user_password==password:
                # user password matched
                return "user password matched"
            return "passwords not matched"
        return "user name not matched"
    return render_template("user_login.html")