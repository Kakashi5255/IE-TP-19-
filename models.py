from sqlalchemy import Column, Integer, BigInteger, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Epic 1: Car ownership
class VehicleRegistration(Base):
    __tablename__ = "vehicle_registrations"

    id = Column(BigInteger, primary_key=True, index=True)
    state = Column(String)
    year_range = Column(String)
    total = Column(Integer)
    percentage = Column(Float)

# Epic 2: Real-time parking availability
class ParkingStatus(Base):
    __tablename__ = "parking_status"

    id = Column(BigInteger, primary_key=True, index=True)
    lastupdated = Column(String)
    status_timestamp = Column(String)
    zone_number = Column(Integer)
    status_description = Column(String)
    kerbsideid = Column(Integer)
    location = Column(String)
