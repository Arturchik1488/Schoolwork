from flask import render_template, request, redirect, url_for, flash, session
from app import app, db, bcrypt
from forms import RegistrationForm, LoginForm, AdminLoginForm
from models import User
from functools import wraps

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/register", methods=['GET', 'POST'])
def register():
    if 'user_id' in session:
        return redirect(url_for('dashboard'))
        
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        
        user = User(
            username=form.username.data,
            email=form.email.data,
            password=hashed_password,
            role="user"
        )
        
        db.session.add(user)
        db.session.commit()
        
        flash('Your account has been created! You can now log in.', 'success')
        return redirect(url_for('login'))
        
    return render_template('register.html', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if 'user_id' in session:
        return redirect(url_for('dashboard'))
        
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            session['user_id'] = user.id
            session['role'] = user.role
            
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Login failed. Please check your email and password.', 'danger')
            
    return render_template('login.html', form=form)

@app.route("/logout")
def logout():
    session.pop('user_id', None)
    session.pop('role', None)
    flash('You have been logged out.', 'info')
    return redirect(url_for('home'))

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Please log in to access this page.', 'warning')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'role' not in session or session['role'] != 'admin':
            flash('You do not have permission to access this page.', 'danger')
            return redirect(url_for('dashboard'))
        return f(*args, **kwargs)
    return decorated_function

@app.route("/dashboard")
@login_required
def dashboard():
    user = User.query.get(session['user_id'])
    is_admin = session.get('role') == 'admin'
    
    return render_template('dashboard.html', user=user, is_admin=is_admin)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route("/admin/login", methods=['GET', 'POST'])
def admin_login():
    if 'user_id' in session and session.get('role') == 'admin':
        return redirect(url_for('dashboard'))
        
    form = AdminLoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        
        if user and user.role == 'admin' and bcrypt.check_password_hash(user.password, form.password.data):
            session['user_id'] = user.id
            session['role'] = 'admin'
            
            flash('Admin login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Admin login failed. Please check your credentials or you may not have admin privileges.', 'danger')
            
    return render_template('admin_login.html', form=form)

@app.cli.command('create-admin')
def create_admin():
    admin = User.query.filter_by(email='admin@example.com').first()
    if not admin:
        hashed_password = bcrypt.generate_password_hash('adminpassword').decode('utf-8')
        admin = User(
            username='admin',
            email='admin@example.com',
            password=hashed_password,
            role='admin'
        )
        db.session.add(admin)
        db.session.commit()
        print('Admin user created successfully!')
    else:
        print('Admin user already exists!')
