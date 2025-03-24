from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)
    role = db.Column(db.String(10), nullable=False, default="user")
    
    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.role}')"
