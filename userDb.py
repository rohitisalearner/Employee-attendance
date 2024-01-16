from datetime import datetime
from sqlalchemy import Column, Integer, ForeignKey
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
class dailyattendance(db.Model):
    __tablename__ = 'dailyattendance'
    Id= db.Column(db.Integer, primary_key=True)
    EmpId = db.Column(db.String(100), unique=False)
    Name= db.Column(db.String(100))
    Date=db.Column(db.DateTime)
    CheckinTime=db.Column(db.DateTime)
    ReferenceID=db.Column(db.String(100), unique=False)
    CheckoutTime = db.Column(db.DateTime)



class employeeinfo(db.Model):
    __tablename__='employeeinfo'
    Id= db.Column(db.Integer, primary_key=True)
    EmpId = db.Column(db.String(100), unique=False)
    Name= db.Column(db.String(100))
    DOJ = db.Column(db.String(100), unique=False)
    Phone=db.Column(db.String(100), unique=False)
    Designation=db.Column(db.String(100), unique=False)
    Email=db.Column(db.String(100), unique=False)