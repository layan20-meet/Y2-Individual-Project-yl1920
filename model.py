from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()
class User(Base):
	__tablename__='User'
	User_num=Column(Integer, primary_key=True)
	Fname = Column(String)
	Lname = Column(String)
	username=Column(String)
	Email=Column(String)
	password=Column(String)

class Travel(Base):
	__tablename__='Travel'
	travel_id=Column(Integer, primary_key=True)
	Travel_name = Column(String)
	Destenation = Column(String)
	Dates=Column(String)
	Ques1=Column(String)
	Ques2=Column(String)
	Ques3=Column(String)
	Ques4=Column(String)
	Ques5=Column(String)
	picture=Column(String)
