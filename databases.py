from model import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///knowledge.db?check_same_thread=False')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def query_all_users():
	users=session.query(User).all()
	return users

def query_all_travels():
	users=session.query(Travel).all()
	return users

def add_User(Fname,Lname,username,Email,password):
	add_User = User(Fname=Fname,
		Lname=Lname, 
		username=username,
		Email=Email,
		password=password)
	session.add(add_User)
	session.commit()
	print("Added user successfully")

def add_Travel(Travel_name,Destenation,Dates,Ques1,Ques2,Ques3,Ques4,Ques5,picture):
	add_Travel = Travel(Travel_name=Travel_name,
		Destenation=Destenation, 
		Dates=Dates,
		Ques1=Ques1,
		Ques2=Ques2,
		Ques3=Ques3,
		Ques4=Ques4,
		Ques5=Ques5,
		picture=picture)
	session.add(add_Travel)
	session.commit()

def delete_travel(id_number):
	session.query(Travel).filter_by(travel_id=id_number).delete()
	session.commit()
    