from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, DataRequired, Email, EqualTo, ValidationError
import email_validator
from market.models import User


class Register_form(FlaskForm):

    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError(message="Username already exists.")

    def validate_email(self, email_to_check):
        email = User.query.filter_by(e_mail=email_to_check.data).first()
        if email:
            raise ValidationError(message="Email already in use")

    username = StringField(label="Create an username", validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField(label="Enter your email", validators=[DataRequired(), Email()])
    password1 = PasswordField(label="Create your password", validators=[DataRequired(), Length(min=2, max=20)])
    password2 = PasswordField(label="Confirm your password", validators=[EqualTo('password1')])
    submit = SubmitField(label="CREATE ACCOUNT")

class Login_form(FlaskForm):

    # def validate_username(self, username_to_check):
    #     user = User.query.filter_by(username=username_to_check.data).first()
    #     if user is None:
    #         raise ValidationError(message="User not found")
    #
    # def validate_password(self, password_to_check):
    #     password = User.query.filter_by(password=password_to_check.data).first()
    #     if password is None:
    #         raise ValidationError(message="Incorrect password")

    username = StringField(label="Enter your username", validators=[DataRequired()])
    password = PasswordField(label="Enter your password", validators=[DataRequired()])
    submit = SubmitField(label="LOGIN")

class Purchase(FlaskForm):
    submit = SubmitField(label="Purchase item")

class Sell(FlaskForm):
    submit = SubmitField(label="Sell item")

