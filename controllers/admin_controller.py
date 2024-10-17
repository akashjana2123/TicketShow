from flask import current_app as app, render_template, request
from models import *


@app.route("/admin_login", methods=["GET", "POST"])
def admin_login():
    if request.method=="POST":
        admin_name=request.form.get("admin_name")
        admin_obj=Admin.query.get(admin_name)
        password=request.form.get("admin_password")
        print(f"admin_name received:{admin_name}, admin password from form:{password}")
        if admin_obj:
            # admin name matched
            if admin_obj.admin_password==password:
                # admin password matched
                return "admin password matched"
            return "passwords not matched"
        return "admin name not matched"
    return render_template("admin_login.html")