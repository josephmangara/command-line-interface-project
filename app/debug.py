#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine('sqlite:///library_management_sysem.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    import ipdb; ipdb.set_trace()