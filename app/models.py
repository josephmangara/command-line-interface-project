#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import (Column, ForeignKey, String, Integer)

engine = create_engine('sqlite:///library_management_system.db')

Base = declarative_base()

class Library(Base):

    __tablename__ = "libraries"
    id = Column(Integer(), primary_key=True)
    name = Column(String)
    location = Column(String)
    address = Column(String)

    def __repr__(self):
        return f"Library {self.id}: " \
            + f"{self.name}, " \
            + f"{self.address}" \
            + f"{self.location}"

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer(), primary_key=True)
    author = Column(String)
    title = Column(String)
    edition = Column(String)
    condition = Column(String)

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer(), primary_key=True)
    first_name = Column(String)
    last_name =  Column(String)
    contact_info = Column(Integer)

