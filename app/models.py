#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///library_management_sysem.db')

Base = declarative_base

class Library(Base):

    __tablename__ = "library"

class Books(Base):
    __tablename__ = 'books'

class users(Base):
    __tablename__ = 'users'