
from flask_script import Manager,Server
from app import create_app,db
<<<<<<< HEAD
from flask_bootstrap import Bootstrap
=======
>>>>>>> 67526690324b2686fd6e0a76a7df02d3d0865bd2

app = create_app('default')

manager = Manager(app)

<<<<<<< HEAD
manager = Manager(app)
manager.add_command('server', Server)

@manager.shell
def make_shell_context():
    return dict(app=app, db=db, User=User)

if __name__ == '__main__':
    app.secret_key='dush'
    manager.run()
=======
manager.add_command('server', Server)

if __name__ == '__main__':
    manager.run()

>>>>>>> 67526690324b2686fd6e0a76a7df02d3d0865bd2
