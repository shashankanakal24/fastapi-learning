from sqlalchemy import Column, String, Integer, Float, JSON

from app.core.database import Base


class Patient(Base):

    __tablename__ = "patients"

    id = Column(String(20), primary_key=True)

    name = Column(String(100))

    age = Column(Integer)

    gender = Column(String(20))

    height = Column(Float)

    weight = Column(Float)

    email = Column(String(100))

    contact = Column(JSON)

    allergies = Column(JSON)

    address = Column(JSON)