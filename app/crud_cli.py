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
def list_books():
    """List all books"""
    books = session.query(Book).all()
    for book in books:
        print(book)

if __name__ == '__main__':
    cli()
