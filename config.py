class Config:
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://liz:aschenbrenner@localhost/blog'
    SQLALCHEMY_TRACK_MODIFICATIONS=False

class ProdConfig(Config):
    #SQLALCHEMY_DATABASE = os.environ.get("DATABASE_URL")
    pass

class DevConfig(Config):

    DEBUG = True

config_options ={
"production":ProdConfig,
"default":DevConfig
}
