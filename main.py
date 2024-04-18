from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def home():
    return ("Welcome to homepage")

@app.route('/admin')
def admin():
    return render_template("/admin/admin.html")

@app.route('/admin/login')
def login():
    return render_template("/admin/login.html")

@app.route('/admin/register')
def register():
    return render_template("/admin/register.html")

@app.errorhandler(404)
def path_to_error(e):
    return render_template ("/error/404.html"), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

