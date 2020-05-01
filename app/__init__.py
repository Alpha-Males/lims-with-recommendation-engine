from flask import Flask 
from sqlalchemy import create_engine,and_
from sqlalchemy.orm import sessionmaker,scoped_session

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text


engine=create_engine("mysql+pymysql://prince:@localhost/rohit")
                    #(mysql)

db=scoped_session(sessionmaker(bind=engine))

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://prince:@localhost/rohit'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True

db1=SQLAlchemy(app)

from app import routes

