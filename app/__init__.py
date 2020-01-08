from flask import Flask
from .config import config_options
from flask_bootstrap import Bootstrap
from .main import main as main_blueprint
from .request import configure_request

bootstrap = Bootstrap()

 
# Initializing application
def create_app(config_name):
    app = Flask(__name__)

    # Setting up configuration
    app.config.from_object(config_options[config_name])
    app.register_blueprint(main_blueprint)

    
    # Initializing flask extensions
    bootstrap.init_app(app)
    
    
    
    return app

