from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField, EmailField, PasswordField, FloatField, TextAreaField,FileField
from wtforms.validators import DataRequired 

class RegisterForm(FlaskForm):
    username = StringField("Username: ", validators=[DataRequired()])
    email = EmailField("Email: ", validators=[DataRequired()])
    password = PasswordField("Password: ", validators=[DataRequired()])
    submit = SubmitField("Submit")

class LoginForm(FlaskForm):
    username = StringField("Username: ", validators=[DataRequired()])
    password = PasswordField("Password: ", validators=[DataRequired()])
    submit = SubmitField("Submit")

class ProductForm(FlaskForm):
    name = StringField("Name: ", validators=[DataRequired()])
    category = StringField("Category: ", validators=[DataRequired()])
    price = FloatField("Price: ", validators=[DataRequired()])
    image = FileField("Image: ",name='file', validators=[DataRequired()])
    description = TextAreaField("Description: ", validators=[DataRequired()])
    submit = SubmitField("Submit")
