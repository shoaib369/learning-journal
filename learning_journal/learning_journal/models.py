from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    )

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()


class MyModel(Base):
    __tablename__ = 'models'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    value = Column(Integer)

Index('my_index', MyModel.name, unique=True, mysql_length=255)

class Entry(Base):
    __tablename__ = 'entries'
    id = Column(Integer, primary_key = True);
    title = Column(unique=True, Unicode(255), nullable = False)
    body = Column(UnicodeText, default = 'u')
    created = Column(DateTime, nullable = False, default = datetime.datetime.utcnow())
    edited = Column(DateTime, nullable = False, default = datetime.datetime.now(), onupdate=datetime.datetime.utcnow())

    @classmethod
    def all(cls, session = None):
        for row in Session.query(Entry).order_by(Entry.edited)
            print(row.title, row.body, row.created, row.edited)

    @classmethod
    def by_id(cls, id, session = None):
        if session is None:
            session = DBSession
        return session.query(cls).get(id)