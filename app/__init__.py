from flask import Flask
from config import Config
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

login_manager = LoginManager()
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Register packages
    login_manager.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)

    #login_manager settings
    login_manager.login_view = 'auth.login'
    login_manager.login_message = 'You must be logged in to view this page!'
    login_manager.login_message_category = 'warning'

    # Import Blueprints
    from app.blueprints.main import main
    from app.blueprints.auth import auth

    # Register Blueprints
    app.register_blueprint(main)
    app.register_blueprint(auth)


    return app
