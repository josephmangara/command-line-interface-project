#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Table, Column, ForeignKey, String, Integer

engine = create_engine('sqlite:///library_management_system.db')

Base = declarative_base()

class Library(Base):

    __tablename__ = "libraries"
    id = Column(Integer(), primary_key=True)
    name = Column(String)
    location = Column(String)
    address = Column(String)

    staff = relationship('Staff', backref=backref('library'))
    books = relationship('Book', back_populates='library')

    def __repr__(self):
        return f"Library {self.id}: " \
            + f"{self.name}, " \
            + f"{self.address}" 
    
    def borrowed_books(self):
        pass

class Staff(Base):
    __tablename__ = 'staff'

    id = Column(Integer(), primary_key=True)
    first_name = Column(String)
    last_name =  Column(String)
    position = Column(String)
    salary = Column(Integer)
    employee_id = Column(Integer)
    staff_library_id = Column(Integer(), ForeignKey('libraries.id'))

    def __repr__(self):
        return f"User {self.id}: " \
               + f"{self.first_name} {self.last_name}, " \
               + f"Position: {self.position}" \
               + f"Id: {self.employee_id}" \
               + f"Salary: {self.salary}"

association_table = Table('association', Base.metadata,
    Column('my_library_id', Integer, ForeignKey('libraries.id')),
    Column('my_reader_id', Integer, ForeignKey('readers.id')),
    Column('my_book_id', Integer, ForeignKey('books.id'))
)                          

class Reader(Base):
    __tablename__ = 'readers'

    id = Column(Integer(), primary_key=True)
    first_name = Column(String)
    last_name =  Column(String)
    contact_info = Column(String)

    reader_library_id = Column(Integer(), ForeignKey('libraries.id'))
    books = relationship('Book', secondary=association_table, back_populates='readers')

    def __repr__(self):
        return f"User {self.id}: " \
               + f"{self.first_name} {self.last_name}, " \
               + f"Contact Info: {self.contact_info}"

    def borrowed_a_book(self):
        pass 

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer(), primary_key=True)
    author = Column(String)
    title = Column(String)
    edition = Column(String)
    condition = Column(String)
    library_id = Column(Integer, ForeignKey('libraries.id'))
    reader_id = Column(Integer, ForeignKey('readers.id'))

    def __repr__(self):
        return f"Book {self.id}: " \
               + f"{self.title} by {self.author}, " \
               + f"Edition: {self.edition}, " \
               + f"Condition: {self.condition}"
