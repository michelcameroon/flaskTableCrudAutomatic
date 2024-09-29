#from flask_sqlalchemy import SQLAlchemy

from app import db
#db = SQLAlchemy()  # Assuming you have already initialized SQLAlchemy

class YourModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # Other columns (e.g., name, email)
    # ...
    firstName = db.Column(db.String(20))
    lastName = db.Column(db.String(20))
    
    def __repr__(self):
        return f'<YourModel {self.id}>'


    def __init__(self, firstName, lastName):
        self.firstName=firstName
        self.lastName=lastName

