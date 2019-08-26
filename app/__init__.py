from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail
#local imports

from config import Config

db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
mail = Mail()
#create the app factory
def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)
    migrate.init_app(app,db)
    login.init_app(app)
    mail.init_app(app)
    #register blueprints here
    from app.models import User
    
    return app
