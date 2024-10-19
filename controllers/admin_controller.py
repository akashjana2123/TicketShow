from flask import current_app as app, render_template, request, redirect
from models import *


logged_admin=None
unauthorized_error=False

@app.route("/admin_login", methods=["GET", "POST"])
def admin_login():
    error=None
    if request.method=="POST":
        admin_name=request.form.get("admin_name")
        admin_obj=Admin.query.get(admin_name)
        password=request.form.get("admin_password")
        if admin_obj:
            # admin name matched
            if admin_obj.admin_password==password:
                # admin password matched
                global logged_admin
                logged_admin=admin_name
                return redirect("admin_dashboard")
            error="passwords not matched"
        else:
            error="admin name not matched"
    global unauthorized_error
    if unauthorized_error:
        error="Please sign in as an admin first"
        unauthorized_error=False
    return render_template("admin_login.html", error=error)

def check_login():
    global logged_admin
    if not logged_admin:
        global unauthorized_error
        unauthorized_error=True
        return redirect("admin_login")

@app.route("/admin_dashboard")
def admin_dashboard():
    check_login()
    return render_template("admin_dashboard.html")

@app.route("/venue_create", methods=["GET", "POST"])
def venue_create():
    check_login()
    if request.method=="POST":
        # fetch data from html
        venue_name=request.form.get("venue_name")
        venue_location=request.form.get("venue_location")
        new_venue=Venue(venue_name=venue_name, venue_location=venue_location)
        db.session.add(new_venue)
        db.session.commit()
        return redirect("admin_dashboard")
    return render_template("venue_create.html")

@app.route("/venue_delete", methods=["GET", "POST"])
def venue_delete():
    check_login()
    if request.method=="POST":
        # fetch data from html
        venue_name=request.form.get("venue_name")
        venue_location=request.form.get("venue_location")
        new_venue=Venue(venue_name=venue_name, venue_location=venue_location)
        db.session.add(new_venue)
        db.session.commit()
        return redirect("admin_dashboard")
    venues=Venue.query.all()
    return render_template("venue_delete.html", venues=venues)