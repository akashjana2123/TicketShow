from flask import current_app as app, render_template, request, redirect
from models import *


logged_admin=None
unauthorized_error=False

# Admin Login

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

# Admin dashboard


@app.route("/admin_dashboard")
def admin_dashboard():
    check_login()
    return render_template("admin_dashboard.html")

#Venue

#Create a venue

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

#Edit venue

@app.route("/venue_edit", methods=["GET", "POST"])
def venue_edit():
    check_login()
    if request.method=="POST":
        # fetch data from html
        venue_name=request.form.get("venue_name")
        venue_location=request.form.get("venue_location")
        existing_venue=Venue.query.get(request.form.get("venue_id"))
        existing_venue.venue_name=venue_name
        existing_venue.venue_location=venue_location
        db.session.commit()
        return redirect("admin_dashboard")
    return render_template("venue_edit.html",venues=Venue.query.all())

#Delete venue

@app.route("/venue_delete", methods=["GET", "POST"])
def venue_delete():
    check_login()
    if request.method=="POST":
        # fetch data from html
        venue_id=request.form.get("venue_id")
        venue_obj_to_delete=Venue.query.get(venue_id)
        db.session.delete(venue_obj_to_delete)
        db.session.commit()
        return redirect("admin_dashboard")
    venues=Venue.query.all()
    return render_template("venue_delete.html", venues=venues)

#Movie

#Create a Movie

@app.route("/movie_create", methods=["GET", "POST"])
def movie_create():
    check_login()
    if request.method=="POST":
        # fetch data from html
        movie_name=request.form.get("movie_name")
        new_movie=Movie(movie_name=movie_name)
        db.session.add(new_movie)
        db.session.commit()
        return redirect("admin_dashboard")
    return render_template("movie_create.html")

#Edit a Movie

@app.route("/movie_edit", methods=["GET", "POST"])
def movie_edit():
    check_login()
    if request.method=="POST":
        # fetch data from html
        movie_name=request.form.get("movie_name")
        movie_location=request.form.get("movie_location")
        existing_movie=Movie.query.get(request.form.get("movie_id"))
        existing_movie.movie_name=movie_name
        existing_movie.movie_location=movie_location
        db.session.commit()
        return redirect("admin_dashboard")
    return render_template("movie_edit.html",movies=Movie.query.all())

#delete a Movie

@app.route("/movie_delete", methods=["GET", "POST"])
def movie_delete():
    check_login()
    if request.method=="POST":
        # fetch data from html
        movie_id=request.form.get("movie_id")
        movie_obj_to_delete=Movie.query.get(movie_id)
        db.session.delete(movie_obj_to_delete)
        db.session.commit()
        return redirect("admin_dashboard")
    movies=Movie.query.all()
    return render_template("movie_delete.html", movies=movies)

#Relations

@app.route("/relation_management", methods=["GET", "POST"])
def relation_management():
    check_login()
    if request.method=="POST":
        venue_id=request.form.get("venue_id")
        venue_obj=Venue.query.get(venue_id)
        assigned_movie_id_list=request.form.getlist("assigned_movies")
        price_list=dict([(movie_id, request.form.get(f"price_{movie_id}")) for movie_id in assigned_movie_id_list])
        print(price_list)
        # venue_obj.venue_movies=[Movie.query.get(int(movie_id)) for movie_id in assigned_movie_id_list]
        db.session.commit()
        return redirect("admin_dashboard")
    venues=Venue.query.all()
    movies=Movie.query.all()
    all_movie_ids=set([movie.movie_id for movie in movies])
    obj_to_return=[]
    for venue in venues:
        related_movie_ids=set([movie.movie_id for movie in venue.venue_movies])
        unchecked_movie_ids=all_movie_ids-related_movie_ids
        unchecked_movie_objs=[Movie.query.get(movie_id) for movie_id in unchecked_movie_ids]
        obj_to_return.append({"venue":venue, "unchecked_movies":unchecked_movie_objs})
    return render_template("relation_management.html", return_obj=obj_to_return)