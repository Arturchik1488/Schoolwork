from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo, Email, ValidationError
from models import User

class RegistrationForm(FlaskForm):
    username = StringField('Username', 
                          validators=[DataRequired(), Length(min=3, max=120)],
                          render_kw={"placeholder": "Enter Username", "class": "form-control"})
    email = StringField('Email',
                        validators=[DataRequired(), Email()],
                        render_kw={"placeholder": "Enter Email", "class": "form-control"})
    password = PasswordField('Password',
                            validators=[DataRequired(), Length(min=6)],
                            render_kw={"placeholder": "Enter Password", "class": "form-control"})
    confirm_password = PasswordField('Confirm Password',
                                    validators=[DataRequired(), EqualTo('password')],
                                    render_kw={"placeholder": "Confirm Password", "class": "form-control"})
    submit = SubmitField('Sign Up', render_kw={"class": "btn btn-primary"})
    
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username already taken. Please choose a different one.')
            
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email already registered. Please use a different one.')

class LoginForm(FlaskForm):
    email = StringField('Email',
                       validators=[DataRequired(), Email()],
                       render_kw={"placeholder": "Enter Email", "class": "form-control"})
    password = PasswordField('Password',
                            validators=[DataRequired()],
                            render_kw={"placeholder": "Enter Password", "class": "form-control"})
    submit = SubmitField('Login', render_kw={"class": "btn btn-primary"})
    
class AdminLoginForm(FlaskForm):
    username = StringField('Admin Username',
                         validators=[DataRequired()],
                         render_kw={"placeholder": "Enter Admin Username", "class": "form-control"})
    password = PasswordField('Password',
                            validators=[DataRequired()],
                            render_kw={"placeholder": "Enter Admin Password", "class": "form-control"})
    submit = SubmitField('Admin Login', render_kw={"class": "btn btn-danger"})
