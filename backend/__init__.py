from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config
from backend.db import db



def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    app.config.from_pyfile("../config.py")


    db.init_app(app)

    from backend.users.controller import users
    from backend.categories.controller import categories
    from backend.regions.controller import regions
    from backend.districts.controller import districts

    #registering blueprints    
    app.register_blueprint(users)
    app.register_blueprint(categories)
    app.register_blueprint(regions)
    app.register_blueprint(districts)
  

   
    return app