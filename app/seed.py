from faker import Faker
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Library, Book, Reader, Staff
from barnum import gen_data

if __name__ == '__main__':
    engine = create_engine('sqlite:///library_management_system.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    session.query(Library).delete()
    session.query(Book).delete()
    session.query(Reader).delete()
    session.query(Staff).delete()

    fake = Faker()

    # Add libraries
    libraries = []
    for i in range(2):
        library = Library(
            name=gen_data.create_company_name(biz_type="Library"),
            address=gen_data.create_city_state_zip()
        )

        session.add(library)
        libraries.append(library)
     # Add and commit all restaurants at once
    session.commit()

    # Add staff
    staff = []
    for i in range(5):
        employee = Staff(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            position=gen_data.create_job_title(),
            salary=random.randint(24000, 84000),
            employee_id=random.randint(3444, 4192)
        )
        session.add(employee)
        staff.append(employee)

    session.commit()

    # Add readers 
    readers = []
    for i in range(12):
        reader = Reader(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            contact_info=gen_data.create_email()
        )
        session.add(reader)
        readers.append(reader)

    session.commit()

    # Add books 
    books = []
    desired_book_count = 45
    books_created = 0

    for library in libraries:
        for reader in readers:
            if books_created < desired_book_count:
                book = Book(
                    author=gen_data.create_name(),
                    title=gen_data.create_nouns(max=5),
                    edition=gen_data.create_date(past=True),
                    condition=random.choice(['new', 'used']),
                    library=library  
                )
                session.add(book)
                books.append(book)
                books_created += 1
            else:
                break

    session.commit()