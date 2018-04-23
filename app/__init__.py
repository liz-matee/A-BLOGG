
from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

bootstrap = Bootstrap()
db = SQLAlchemy()

def create_app(config_state):

    app = Flask(__name__)
    app.config['SQLAlchemy_HOST'] = 'localhost'
    app.config['SQLAlchemy_USER'] = 'root'
    app.config['SQLAlchemy_PASSWORD'] = 'aschenbrenner'
    app.config['SQLAlchemy_DB'] = 'blog'
    app.config['SQLAlchemy_CURSORCLASS'] = 'DictCursor'

    sqlalchemy = SQLAlchemy(app)

    app.config.from_object(config_options[config_state])


    bootstrap.init_app(app)
    db.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)


    return app
