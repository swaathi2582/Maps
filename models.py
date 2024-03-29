import os
from extensions import db
from uuid import uuid4
from werkzeug.security import generate_password_hash,check_password_hash


SQLALCHEMY_DATABASE_URI = os.environ['FLASK_SQLALCHEMY_DATABASE_URI']

class User(db.Model):
    __tablename__ = 'user_table'

    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(30))
    password = db.Column(db.String(200))

    #__repr__ method allows you to customize how instances of your class are displayed
    def __repr__(self):
        return f"<User {self.username}>"
    
    #to get user using username
    def get_user_by_username(cls,username):
        return cls.query.filter_by(username=username).first()
    
    #to save the user
    def save(self):
        db.session.add(self)
        db.session.commit()

    # to remove a user
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    #Generating hashed password and storing it in db
    def generating_hashed_password(self,password):
        self.password = generate_password_hash(password)

    def checking_hashed_password(self,password):
        return check_password_hash(self.password,password)
    

        
