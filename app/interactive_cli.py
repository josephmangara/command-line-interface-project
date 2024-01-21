#!/usr/bin/env python3
# backup python GUI lms

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Library, Staff, Reader, Book

DATABASE_URI = 'sqlite:///library_management_system.db'

engine = create_engine(DATABASE_URI)
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

def get_session():
    return DBSession()

# Library commands in interactive mode 
def add_library_interactive():
    """Interactive mode for adding a library"""
    name = input("Enter library name: ")
    location = input("Enter library location: ")
    address = input("Enter library address: ")

    try:
        with get_session() as session:
            new_library = Library(name=name, location=location, address=address)
            session.add(new_library)
            session.commit()
            print(f"Library '{name}' added successfully.")
    except Exception as e:
        print(f"Error: {e}")

def list_libraries_interactive():
    """Interactive mode for listing all libraries"""
    try:
        with get_session() as session:
            libraries = session.query(Library).all()
            for library in libraries:
                print(library)
    except Exception as e:
        print(f"Error: {e}")

def update_library_interactive():
    """Interactive mode for updating a library"""
    library_id = int(input("Enter library ID to update: "))
    name = input("Enter new library name: ")
    location = input("Enter new library location: ")
    address = input("Enter new library address: ")

    try:
        with get_session() as session:
            library = session.query(Library).get(library_id)
            if library:
                library.name = name
                library.location = location
                library.address = address
                session.commit()
                print(f"Library with ID {library_id} updated successfully.")
            else:
                print(f"Library with ID {library_id} not found.")
    except Exception as e:
        print(f"Error: {e}")

def delete_library_interactive():
    """Interactive mode for deleting a library"""
    library_id = int(input("Enter library ID to delete: "))

    try:
        with get_session() as session:
            library = session.query(Library).get(library_id)
            if library:
                session.delete(library)
                session.commit()
                print(f"Library with ID {library_id} deleted successfully.")
            else:
                print(f"Library with ID {library_id} not found.")
    except Exception as e:
        print(f"Error: {e}")

# Staff commands in interactive mode
def add_employee_interactive():
    """Interactive mode for adding an employee"""
    first_name = input("Enter employee first name: ")
    last_name = input("Enter employee last name: ")
    position = input("Enter employee position: ")
    salary = input("Enter employee salary: ")
    employee_id = input("Enter employee ID: ")

    try:
        with get_session() as session:
            new_employee = Staff(first_name=first_name, last_name=last_name, position=position, salary=salary, employee_id=employee_id)
            session.add(new_employee)
            session.commit()
            print(f"Employee added successfully.")
    except Exception as e:
        print(f"Error: {e}")

def list_staff_interactive():
    """Interactive mode for listing all staff"""
    try:
        with get_session() as session:
            staff = session.query(Staff).all()
            for employee in staff:
                print(employee)
    except Exception as e:
        print(f"Error: {e}")

def update_staff_interactive():
    """Interactive mode for updating an employee"""
    staff_id = int(input("Enter employee ID to update: "))
    first_name = input("Enter new first name: ")
    last_name = input("Enter new last name: ")
    position = input("Enter new position: ")
    salary = input("Enter new salary: ")
    employee_id = input("Enter new employee ID: ")

    try:
        with get_session() as session:
            employee = session.query(Staff).get(staff_id)
            if employee:
                employee.first_name = first_name
                employee.last_name = last_name
                employee.position = position
                employee.salary = salary
                employee.employee_id = employee_id
                session.commit()
                print(f"Employee with ID {staff_id} updated successfully.")
            else:
                print(f"Employee with ID {staff_id} not found.")
    except Exception as e:
        print(f"Error: {e}")

def delete_staff_interactive():
    """Interactive mode for deleting an employee"""
    staff_id = int(input("Enter employee ID to delete: "))

    try:
        with get_session() as session:
            employee = session.query(Staff).get(staff_id)
            if employee:
                session.delete(employee)
                session.commit()
                print(f"Employee with ID {staff_id} deleted successfully.")
            else:
                print(f"Employee with ID {staff_id} not found.")
    except Exception as e:
        print(f"Error: {e}")

 # Interactive mode functions for Readers
def list_readers_interactive():
    """Interactive mode for listing all readers"""
    try:
        with get_session() as session:
            readers = session.query(Reader).all()
            for reader in readers:
                print(reader)
    except Exception as e:
        print(f"Error: {e}")

def add_reader_interactive():
    """Interactive mode for adding a reader"""
    first_name = input("Enter reader's first name: ")
    last_name = input("Enter reader's last name: ")
    contact_info = input("Enter reader's contact info: ")

    try:
        with get_session() as session:
            new_reader = Reader(first_name=first_name, last_name=last_name, contact_info=contact_info)
            session.add(new_reader)
            session.commit()
        print(f"Reader '{first_name} {last_name}' added successfully.")
    except Exception as e:
        print(f"Error: {e}")

def update_reader_interactive():
    """Interactive mode for updating a reader"""
    reader_id = int(input("Enter reader ID to update: "))
    first_name = input("Enter new first name: ")
    last_name = input("Enter new last name: ")
    contact_info = input("Enter new contact info: ")

    try:
        with get_session() as session:
            reader = session.query(Reader).get(reader_id)
            if reader:
                reader.first_name = first_name
                reader.last_name = last_name
                reader.contact_info = contact_info
                session.commit()
                print(f"Reader with ID {reader_id} updated successfully.")
            else:
                print(f"Reader with ID {reader_id} not found.")
    except Exception as e:
        print(f"Error: {e}")

def delete_reader_interactive():
    """Interactive mode for deleting a reader"""
    reader_id = int(input("Enter reader ID to delete: "))

    try:
        with get_session() as session:
            reader = session.query(Reader).get(reader_id)
            if reader:
                session.delete(reader)
                session.commit()
                print(f"Reader with ID {reader_id} deleted successfully.")
            else:
                print(f"Reader with ID {reader_id} not found.")
    except Exception as e:
        print(f"Error: {e}")

# Interactive mode functions for Books
def list_books_interactive():
    """Interactive mode for listing all books"""
    try:
        with get_session() as session:
            books = session.query(Book).all()
            for book in books:
                print(book)
    except Exception as e:
        print(f"Error: {e}")

def add_book_interactive():
    """Interactive mode for adding a book"""
    author = input("Enter book author: ")
    title = input("Enter book title: ")
    edition = input("Enter book edition: ")
    condition = input("Enter book condition: ")

    try:
        with get_session() as session:
            new_book = Book(author=author, title=title, edition=edition, condition=condition)
            session.add(new_book)
            session.commit()
        print(f"Book '{title}' added successfully.")
    except Exception as e:
        print(f"Error: {e}")

def update_book_interactive():
    """Interactive mode for updating a book"""
    book_id = int(input("Enter book ID to update: "))
    author = input("Enter new author: ")
    title = input("Enter new title: ")
    edition = input("Enter new edition: ")
    condition = input("Enter new condition: ")

    try:
        with get_session() as session:
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
    except Exception as e:
        print(f"Error: {e}")

def delete_book_interactive():
    """Interactive mode for deleting a book"""
    book_id = int(input("Enter book ID to delete: "))

    try:
        with get_session() as session:
            book = session.query(Book).get(book_id)
            if book:
                session.delete(book)
                session.commit()
                print(f"Book with ID {book_id} deleted successfully.")
            else:
                print(f"Book with ID {book_id} not found.")
    except Exception as e:
        print(f"Error: {e}")
        


# Interactive mode
def interactive_mode():
    """Enter interactive mode"""
    while True:
        print("\nSelect an option:")
        print("1. Add Library")
        print("2. List Libraries")
        print("3. Update Library")
        print("4. Delete Library")
        print("5. Add Employee")
        print("6. List Staff")
        print("7. Update Staff")
        print("8. Delete Staff")
        print("9. Add Reader")
        print("10. List Readers")
        print("11. Update Reader")
        print("12. Delete Reader")
        print("13. Add Book")
        print("14. List Books")
        print("15. Update Book")
        print("16. Delete Book")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '0':
            break
        elif choice == '1':
            add_library_interactive()
        elif choice == '2':
            list_libraries_interactive()
        elif choice == '3':
            update_library_interactive()
        elif choice == '4':
            delete_library_interactive()
        elif choice == '5':
            add_employee_interactive()
        elif choice == '6':
            list_staff_interactive()
        elif choice == '7':
            update_staff_interactive()
        elif choice == '8':
            delete_staff_interactive()
        elif choice == '9':
            add_reader_interactive()
        elif choice == '10':
            list_readers_interactive()
        elif choice == '11':
            update_reader_interactive()
        elif choice == '12':
            delete_reader_interactive()
        elif choice == '13':
            add_book_interactive()
        elif choice == '14':
            list_books_interactive()
        elif choice == '15':
            update_book_interactive()
        elif choice == '16':
            delete_book_interactive()
        

if __name__ == '__main__':
    interactive_mode()
