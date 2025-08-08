from sqlalchemy import Column, Integer, BigInteger, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class VehicleRegistration(Base):
    __tablename__ = "vehicle_registrations"

    id = Column(BigInteger, primary_key=True, index=True)
    state = Column(String)
    year_range = Column(String)
    total = Column(Integer)
    percentage = Column(Float)
