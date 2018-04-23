
from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

<<<<<<< HEAD
=======

>>>>>>> 67526690324b2686fd6e0a76a7df02d3d0865bd2
bootstrap = Bootstrap()
db = SQLAlchemy()

def create_app(config_state):
<<<<<<< HEAD

    app = Flask(__name__)
    app.config['SQLAlchemy_HOST'] = 'localhost'
    app.config['SQLAlchemy_USER'] = 'root'
    app.config['SQLAlchemy_PASSWORD'] = 'aschenbrenner'
    app.config['SQLAlchemy_DB'] = 'blog'
    app.config['SQLAlchemy_CURSORCLASS'] = 'DictCursor'

    sqlalchemy = SQLAlchemy(app)

=======
    app = Flask(__name__)
>>>>>>> 67526690324b2686fd6e0a76a7df02d3d0865bd2
    app.config.from_object(config_options[config_state])


    bootstrap.init_app(app)
    db.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

<<<<<<< HEAD

=======
>>>>>>> 67526690324b2686fd6e0a76a7df02d3d0865bd2
    return app
