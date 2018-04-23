
from flask_script import Manager,Server
from app import create_app,db
from flask_bootstrap import Bootstrap
from  flask_migrate import Migrate, MigrateCommand

app = create_app('production')
manager = Manager(app)
migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)
manager.add_command('server', Server)

@manager.shell
def make_shell_context():
    return dict(app=app, db=db, User=User)

if __name__ == '__main__':
    app.secret_key='dush'
    manager.run()
