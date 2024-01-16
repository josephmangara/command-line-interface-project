# command-line-interface-project

This command-line interface (CLI) allows you to manage a library management system. You can perform various CRUD operations such as adding libraries, listing libraries, updating libraries, deleting libraries, listing books, and adding books.

My models represent entities such as libraries, staff, readers, and books, along with their relationships.

## Models
1. Library:
Attributes:

id: Primary key for the library.
name: Name of the library.
location: Location of the library.
address: Address of the library.
Relationships:

staff: One-to-Many relationship with Staff.
books: One-to-Many relationship with Book.

2. Staff:
Attributes:

id: Primary key for the staff member.
first_name: First name of the staff member.
last_name: Last name of the staff member.
position: Position or role of the staff member.
salary: Salary of the staff member.
employee_id: Employee ID of the staff member.
staff_library_id: Foreign key referencing the library to which the staff member belongs.
Relationships:

library: Many-to-One relationship with Library.

3. Reader:
Attributes:

id: Primary key for the reader.
first_name: First name of the reader.
last_name: Last name of the reader.
contact_info: Contact information of the reader.
Relationships:

books: Many-to-Many relationship with Book through the association_table.

4. Book:
Attributes:

id: Primary key for the book.
author: Author of the book.
title: Title of the book.
edition: Edition of the book.
condition: Condition of the book.
library_id: Foreign key referencing the library to which the book belongs.
reader_id: Foreign key referencing the reader who borrowed the book.
Relationships:

library: Many-to-One relationship with Library.
readers: Many-to-Many relationship with Reader through the association_table.

5. Association Table:
Table:
association_table: Table defining the many-to-many relationship between Readers and Books.

## Prerequisites

- Python 3
- Required Python packages (install using `pip install -r requirements.txt`):
- Click
- SQLAlchemy

## Installation

1. Clone the repository:
   ```bash
   git@github.com:josephmangara/command-line-interface-project.git

2. install the required packages
   pipenv install
   pipenv shell

3. create the database

## Usage
Run the following commands on terminal:
#### run python3 crud_cli.py to see the list of the available commands.
1. Adding a Library
   python3 crud_cli.py add-library

2. Listing Libraries
   python3 crud_cli.py list-libraries

3. Updating a Library
   python3 crud_cli.py update-library <library_id>

4. Deleting a Library
   python3 crud_cli.py delete-library <library_id>

5. Listing staff
   python3 crud_cli.py list-staff

6. Adding Books
   python3 crud_cli.py add-books

7. Listing Books
   python3 crud_cli.py list-books

8. Updating books
   python3 crud_cli.py update-book <book_id>

9. Listing staff
   python3 crud_cli.py list-staff

### Quitting the cli
- Click control + c for linux and windows users and command + c for macOs.

## Adding contributions
If you'd like to contribute to this project, please follow these steps:

1. Fork the repository on GitHub.
2. Clone your forked repository.
3. Create a new branch for your feature: git checkout -b feature-name.
4. Commit your changes: git commit -m 'Add new feature'.
5. Push your changes to your fork: git push origin feature-name.
6. Open a pull request on the original repository.
