from flask import Flask,render_template
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField, EmailField, PasswordField
from wtforms.validators import DataRequired 
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SECRET_KEY'] = "this is a secret"
db = SQLAlchemy(app)

class Admin(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    password = db.Column(db.String(200), nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<username %r>' % self.username

class RegisterForm(FlaskForm):
    username = StringField("Username: ", validators=[DataRequired()])
    email = EmailField("Email: ", validators=[DataRequired()])
    password = PasswordField("Password: ", validators=[DataRequired()])
    submit = SubmitField("Submit")

class LoginForm(FlaskForm):
    username = StringField("Username: ", validators=[DataRequired()])
    password = PasswordField("Password: ", validators=[DataRequired()])
    submit = SubmitField("Submit")

@app.route('/')
def home():
    return ("Welcome to homepage")

@app.route('/admin')
def admin():
    return render_template("/admin/admin.html")

def admin_product():
    return ("Product")

@app.route('/admin/login', methods=['GET', 'POST'])
def login():
    name = None
    password = None
    form = LoginForm()
    return render_template("/admin/login.html", name = name, password = password, form = form)

@app.route('/admin/register', methods=['GET', 'POST'])
def register():
    name = None
    email = None
    password = None
    form = RegisterForm()
    if form.validate_on_submit():
        name = form.username.data
        email = form.email.data
        password = form.password.data
        form.username.data = ''
        form.email.data = ''
        form.password.data = ''
    return render_template("/admin/register.html" , name = name, email = email, password = password, form = form)

@app.errorhandler(404)
def path_to_error(e):
    return render_template ("/error/404.html"), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

