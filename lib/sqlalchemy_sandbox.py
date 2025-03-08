#!/usr/bin/env python3

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base
engine = create_engine('sqlite:///students.db', future=True)
Base = declarative_base()
Session = sessionmaker(bind=engine, future=True) 




class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer(), primary_key=True)
    name = Column(String())

if __name__ == '__main__':
    pass

Base.metadata.create_all(engine)
session = Session()
engine = create_engine('sqlite:///students.db')
Base.metadata.create_all(engine)