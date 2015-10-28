from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from models import Base, User

engine = create_engine("postgresql://sqlalchemy_test:sqlalchemy_test@localhost:5432/sqlalchemy_test", echo=True)
Base.metadata.create_all(engine)


def f():
    Session1 = sessionmaker(bind=engine, autoflush=False)

    session1 = Session1()
    # ed_user = User(name='ed', fullname='Ed Jones', password='edspassword')
    # session1.add(ed_user)
    users = session1.query(User).all()

    session1.close()
    return users


def main():

    users = f()
    print(users[0].name)


if __name__ == '__main__':
    main()
