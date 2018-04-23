
from flask_script import Manager,Server
from app import create_app,db
from flask_bootstrap import Bootstrap

app = create_app('default')

manager = Manager(app)

manager = Manager(app)
manager.add_command('server', Server)

@manager.shell
def make_shell_context():
    return dict(app=app, db=db, User=User)

if __name__ == '__main__':
    app.secret_key='dush'
    manager.run()
manager.add_command('server', Server)

if __name__ == '__main__':
    manager.run()
