from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database.connection import Base

class Doctor(Base):
    _tablename_ = 'doctor'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    speciality = Column(String, nullable=False)
    contact = Column(String, nullable=False)

    patients = relationship("Patient", back_populates="doctor")
