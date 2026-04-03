from sqlalchemy import Column, Integer, String
from database import Base

class TripModel(Base):
    __tablename__ = "trips"

    id = Column(Integer, primary_key=True, index=True)
    destination = Column(String)
    status = Column(String)