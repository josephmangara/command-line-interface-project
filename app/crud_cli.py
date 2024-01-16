#!/usr/bin/env python3
import click
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Library, Staff, Reader, Book

DATABASE_URI = 'sqlite:///library_management_system.db'

engine = create_engine(DATABASE_URI)
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

@click.group()
def cli():
    """Library Management System CLI"""

@cli.command()
@click.option('--name', prompt='Enter library name', help='Name of the library')
@click.option('--location', prompt='Enter library location', help='Location of the library')
@click.option('--address', prompt='Enter library address', help='Address of the library')
def add_library(name, location, address):
    """Add a new library"""
    new_library = Library(name=name, location=location, address=address)
    session.add(new_library)
    session.commit()
    print(f"Library '{name}' added successfully.")

@cli.command()
def list_libraries():
    """List all libraries"""
    libraries = session.query(Library).all()
    for library in libraries:
        print(library)

@cli.command()
@click.argument('library_id', type=int)
@click.option('--name', prompt='Enter new library name', help='New name of the library')
@click.option('--location', prompt='Enter new library location', help='New location of the library')
@click.option('--address', prompt='Enter new library address', help='New address of the library')
def update_library(library_id, name, location, address):
    """Update a library"""
    library = session.query(Library).get(library_id)
    if library:
        library.name = name
        library.location = location
        library.address = address
        session.commit()
        print(f"Library with ID {library_id} updated successfully.")
    else:
        print(f"Library with ID {library_id} not found.")

@cli.command()
@click.argument('library_id', type=int)
def delete_library(library_id):
    """Delete a library"""
    library = session.query(Library).get(library_id)
    if library:
        session.delete(library)
        session.commit()
        print(f"Library with ID {library_id} deleted successfully.")
    else:
        print(f"Library with ID {library_id} not found.")

@cli.command()
def list_staff():
    """List all staff"""
    staff = session.query(Staff).all()
    for employee in staff:
        print(employee)
@cli.command()
@click.option('--first_name', prompt='Enter first name', help='First name of the staff')
@click.option('--last_name', prompt='Enter last name', help='Last name of the staff')
@click.option('--position', prompt='Enter position', help='Employee position')
@click.option('--salary', prompt='Enter salary', help='Employee salary')
@click.option('--employee_id', prompt='Enter employee_id', help='Employee id')

def add_employee(first_name, last_name, position, salary, employee_id):
    """Add employee"""
    new_staff = Staff(first_name=first_name, last_name=last_name, position=position, salary=salary, employee_id=employee_id)
    session.add(new_staff)
    session.commit()
    print(f"Employee added successfully")

@cli.command()
def list_readers():
    """List all readers"""
    reader = session.query(Reader).all()
    for readers in reader:
        print(readers)

@cli.command()
def list_books():
    """List all books"""
    books = session.query(Book).all()
    for book in books:
        print(book)

@cli.command()
@click.option('--author', prompt='Enter book author', help='Author of the book')
@click.option('--title', prompt='Enter book title', help='Title of the book')
@click.option('--edition', prompt='Enter book edition', help='Edition of the book')
@click.option('--condition', prompt='Enter book condition', help='Condition of the book')
def add_books(author, title, edition, condition):
    """Add books"""
    new_book = Book(author=author, title=title, edition=edition, condition=condition)
    session.add(new_book)
    session.commit()
    print(f"Book '{title}' added successfully.")

@cli.command()
@click.argument('book_id', type=int)
@click.option('--author', prompt='Enter new author', help='New author of the book')
@click.option('--title', prompt='Enter new title', help='New title of the book')
@click.option('--edition', prompt='Enter new edition', help='New edition of the book')
@click.option('--condition', prompt='Enter new condition', help='New condition of the book')
def update_book(book_id, author, title, edition, condition):
    """Update a book"""
    book = session.query(Book).get(book_id)
    if book:
        book.author = author
        book.title = title
        book.edition = edition
        book.condition = condition
        session.commit()
        print(f"Book with ID {book_id} updated successfully.")
    else:
        print(f"Book with ID {book_id} not found.")



if __name__ == '__main__':
    cli()
