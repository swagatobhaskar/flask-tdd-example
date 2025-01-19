from flask import Flask
from flask_migrate import Migrate
from os import environ, getenv

from .models import User
from .extensions import db
from .routes import main_bp

from config import DevConfig, ProdConfig

migrate = Migrate()

def create_app():
    app = Flask(__name__)

    env_type = getenv('ENV')
    print("ENV-->", env_type)
    
    if env_type == 'development':
        config = DevConfig
    else:
        config = ProdConfig

    app.config.from_object(config)
    
    db.init_app(app)
    migrate.init_app(app, db)
    app.register_blueprint(main_bp, url_prefix="/")

    return app
