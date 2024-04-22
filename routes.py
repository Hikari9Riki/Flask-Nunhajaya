import os
import uuid
from flask import render_template, request, url_for,redirect
from models import Admin,Catalog,Product
from form import RegisterForm,LoginForm,ProductForm
from werkzeug.utils import secure_filename

def media_create():
    if not os.path.exists('static/images/product'):
        os.makedirs('static/images/product' )
    


def register_routes(app,db):

    @app.route('/')
    def home():
        media_create()
        return ("Welcome to homepage")

    @app.route('/admin')
    def admin():
        return render_template("/admin/admin.html")
    
    @app.route('/admin/product', methods=['GET', 'POST'])
    def admin_product():
        products = Catalog.query.all()
        return render_template("/admin/admin.html", products=products)

    @app.route('/admin/product/change/<int:id>', methods=['GET', 'POST'])
    def product_change(id):
        
        form = ProductForm()
        products = db.session.execute(db.select(Catalog).filter_by(id=id)).scalar_one()

        if form.validate_on_submit():
            media_create()
            products.name = form.name.data
            products.category = form.category.data
            products.price = form.price.data
            products.image = form.image.data
            products.description = form.description.data

            db.session.commit()
            
            form.name.data = ''
            form.category.data = ''
            form.price.data = ''
            form.image.data = ''
            form.description.data = ''
            return redirect(url_for('admin_product')) 

        
        
        form.name.data = products.name
        form.category.data = products.category
        form.price.data = products.price
        form.image.data = products.image
        form.description.data = products.description

        
        return render_template('admin/product_change.html', form = form, id = id)

    @app.route('/admin/product/add' , methods=['GET', 'POST'])
    def product_add():
        name = None
        category = None
        price = None
        image = None
        description = None
        form = ProductForm()

        if form.validate_on_submit():
            name = form.name.data
            category = form.category.data
            price = form.price.data
            file = request.files['file']
            filename = secure_filename(file.filename)
            file_path = os.path.join('static/images/product', filename)
            media_create()
            file.save(file_path)
            image = os.path.join('/images/product', filename)
            description = form.description.data

            menu = Catalog(name = name, category = category, price = price, image = image, description=description)
            form.name.data = ''
            form.category.data = ''
            form.price.data = ''
            form.image.data = ''
            form.description.data = ''

            db.session.add(menu)
            db.session.commit()
            
            return redirect(url_for('admin_product'))
    
        return render_template("/admin/product_add.html" , name = name, category = category, price = price, image = image, description = description, form = form )




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
        admin = Admin.query.all()
        form = RegisterForm()
        if form.validate_on_submit():
            name = form.username.data
            email = form.email.data
            password = form.password.data

            sudo = Admin(username=name, email=email, password = password)
            
            db.session.add(sudo)
            db.session.commit()
            admin = sudo.query.all()
        return render_template("/admin/register.html" , name = name, email = email, password = password, form = form, admin = admin)

    @app.errorhandler(404)
    def path_to_error(e):
        return render_template ("/error/404.html"), 404

        