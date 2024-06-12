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

def create_doctor(session, name, speciality, contact):
    try:
        doctor = Doctor(name=name, speciality=speciality, contact=contact)
        session.add(doctor)
        session.commit()
        print("Doctor created successfully.")
    except Exception as e:
        print("Error occurred while creating doctor:", e)

def list_doctors(session):
    try:
        doctors = session.query(Doctor).all()
        if doctors:
            print("Doctors:")
            for doctor in doctors:
                print(f"ID: {doctor.id}, Name: {doctor.name}, Speciality: {doctor.speciality}, Contact: {doctor.contact}")
        else:
            print("No doctors found.")
    except Exception as e:
        print("Error occurred while listing doctors:", e)
