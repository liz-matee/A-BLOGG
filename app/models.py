class users(db.model);
__tablename__ = 'users'
id  = db.colomn(db.Integer, primary_key=True)
name  = db.colomn(db.String, index=True)
email  = db.colomn(db.String, unique=True, index=True)
username  = db.colomn(db.String, primary_key=True)
password  = db.colomn(db.Integer, index=True)
register_date  = db.colomn(dt.CURRENT_TIMESTAMP, default=current_timestamp.now(tz=None))

def __repr__(self):
    return f'User. {self.username}
