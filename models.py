from main import db

class Admin(db.Model):
    __tablename__ = 'admin'
    admin_name=db.column(db.string, primary_key=True)
    admin_password=db.column(db.string, nullable=False)