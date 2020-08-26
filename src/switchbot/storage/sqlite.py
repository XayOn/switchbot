from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Meter(Base):
    __tablename__ = 'meter_data'

    id = Column(Integer, primary_key=True)
    mac = Column(String)
    model = Column(String)
    mode = Column(String)
    date = Column(String)
    temp = Column(String)
    humidity = Column(String)


def jsonify(result):
    return {x.name: getattr(result, x.name) for x in result.__table__.columns}


class SqlAlchemyStorage:
    def __init__(self, storage):
        self.engine = create_engine(storage)
        Base.metadata.create_all(self.engine)
        session = sessionmaker(bind=self.engine)
        self.session = session()

    def append(self, data):
        for data in data.values():
            self.session.add(Meter(**data))
        self.session.commit()

    def all(self):
        return [jsonify(result) for result in self.session.query(Meter).all()]

    def latest(self):
        return jsonify(
            self.session.query(Meter).order_by(Meter.id.desc()).first())
