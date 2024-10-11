from database import db

class Admin(db.Model):
    __tablename__ = 'admin'
    admin_name=db.Column(db.String, primary_key=True)
    admin_password=db.Column(db.String, nullable=False)