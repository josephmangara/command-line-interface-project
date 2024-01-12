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
def list_libraries():
    """List all libraries"""
    libraries = session.query(Library).all()
    for library in libraries:
        print(library)

@cli.command()
@click.argument('library_id', type=int)
def list_books(library_id):
    """List books in a library"""
    library = session.query(Library).get(library_id)
    if library:
        books = session.query(Book).filter_by(library_id=library_id).all()
        for book in books:
            print(book)
    else:
        print(f"Library with ID {library_id} not found.")


@cli.command()
def list_readers():
    """List all readers and their borrowed books"""
    readers = session.query(Reader).all()
    for reader in readers:
        print(f"{reader}\nBorrowed Books:")
        for book in reader.books:
            print(f"  {book}")
        print("\n")

if __name__ == '__main__':
    cli()
