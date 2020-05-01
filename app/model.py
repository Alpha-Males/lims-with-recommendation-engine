from app import db1

from flask_login import UserMixin

class Users(db1.Model, UserMixin):
    id = db1.Column(db1.Integer, primary_key=True)
    name = db1.Column(db1.String(20), unique=True, nullable=False)
    username= db1.Column(db1.String(120), unique=True, nullable=False)
    password = db1.Column(db1.String(60), nullable=False)
    #image_file = db1.Column(db1.String(20), nullable=False)

    def retuser(self):
        return self.name


    def validate_username(self,username):
        name=Users.query.filter_by(username=username).first()
        if name:
            raise ValidationError('this username is taken please take some other')



    def __repr__(self):
        return f"User('{self.name}', '{self.username}')"

class Usersbook(db1.Model, UserMixin):
    id = db1.Column(db1.Integer, primary_key=True,autoincrement=True)
    username = db1.Column(db1.String(20), nullable=True,primary_key=True)
    bookname= db1.Column(db1.String(120), nullable=True)



    def __repr__(self):
        return f"Usersbook('{self.username}', '{self.bookname}')"

