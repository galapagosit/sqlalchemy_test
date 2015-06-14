
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("postgresql://sqlalchemy_test:sqlalchemy_test@localhost:5432/sqlalchemy_test", echo=True)

Base = declarative_base()

class User(Base):
     __tablename__ = 'users'

     id = Column(Integer, primary_key=True)
     name = Column(String)
     fullname = Column(String)
     password = Column(String)

     def __repr__(self):
         return "<User(name='%s', fullname='%s', password='%s')>" % (
                                self.name, self.fullname, self.password)

Base.metadata.create_all(engine)

def main():
    print('main')
    Session = sessionmaker(bind=engine)
    session = Session()

    ed_user = User(name='ed', fullname='Ed Jones', password='edspassword')
    session.add(ed_user)
    session.commit()

if __name__ == '__main__':
    main()
