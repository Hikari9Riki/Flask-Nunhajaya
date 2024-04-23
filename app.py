from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate # type: ignore

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, template_folder='templates')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./admin.db'
    app.config['SECRET_KEY'] = "this is a secret"


    db.init_app(app)
    migrate = Migrate(app,db)

    from routes import register_routes
    register_routes(app,db)

    

    return app
