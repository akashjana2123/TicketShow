from database import db

class Admin(db.Model):
    __tablename__="admin"
    admin_name=db.Column(db.String, primary_key=True)
    admin_password=db.Column(db.String, nullable=False)

class User(db.Model):
    __tablename__="user"
    user_name=db.Column(db.String, primary_key=True)
    user_password=db.Column(db.String, nullable=False)
    user_tickets=db.relationship("Ticket")


class Movie(db.Model):
    __tablename__="movie"
    movie_name=db.Column(db.String, nullable=False)
    movie_id=db.Column(db.Integer, primary_key=True, autoincrement=True)
    movie_rating=db.Column(db.Numeric(1,1), nullable=False, default=0)
    movie_total_rating=db.Column(db.Numeric, nullable=False, default=0)
    movie_num_ratings=db.Column(db.Integer, nullable=False, default=0)
    movie_tickets=db.relationship("Ticket")
    movie_venues=db.relationship("Venue", secondary="relation", backref="venue_movies")

class Venue(db.Model):
    __tablename__="venue"
    venue_name=db.Column(db.String, nullable=False)
    venue_id=db.Column(db.Integer, primary_key=True, autoincrement=True)
    venue_location=db.Column(db.String, nullable=False)
    venue_tickets=db.relationship("Ticket")


class Relation(db.Model):
    __tablename__="relation"
    movie_id=db.Column(db.Integer, db.ForeignKey("movie.movie_id"), primary_key=True)
    venue_id=db.Column(db.Integer, db.ForeignKey("venue.venue_id"), primary_key=True)
    price=db.Column(db.Numeric(3, 2), nullable=False)

class Ticket(db.Model):
    __tablename__="ticket"
    movie_id=db.Column(db.Integer, db.ForeignKey("movie.movie_id"))
    venue_id=db.Column(db.Integer, db.ForeignKey("venue.venue_id"))
    user_name=db.Column(db.String, db.ForeignKey("user.user_name"))
    ticket_id=db.Column(db.Integer, primary_key=True, autoincrement=True)
    ticket_num_tickets=db.Column(db.Integer, nullable=False)