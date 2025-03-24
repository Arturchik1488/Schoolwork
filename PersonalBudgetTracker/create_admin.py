import os
from app import app, db, bcrypt
from models import User

def create_default_admin():
    """Create a default admin user with preset credentials"""
    print("\n===== Creating Default Admin User =====")
    
    username = "admin"
    email = "admin@example.com"
    password = "adminpass123"
    
    with app.app_context():
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            print(f"Admin user '{username}' already exists.")
            return False
        
        try:
            hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
            admin = User(
                username=username,
                email=email,
                password=hashed_password,
                role='admin'
            )
            db.session.add(admin)
            db.session.commit()
            
            print(f"\nDefault admin user created successfully!")
            print(f"Username: {username}")
            print(f"Email: {email}")
            print(f"Password: {password}")
            print(f"You can now log in using the admin login page.")
            return True
        except Exception as e:
            print(f"Error creating admin user: {str(e)}")
            return False

if __name__ == "__main__":
    create_default_admin()