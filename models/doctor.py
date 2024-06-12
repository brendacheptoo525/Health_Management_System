from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database.connection import Base

class Doctor(Base):
    __tablename__ = 'doctor'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    speciality = Column(String, nullable=False)
    contact = Column(String, nullable=False)

    patients = relationship("Patient", back_populates="doctor")

     @classmethod
    def find_by_id(cls, session, doctor_id):
        return session.query(cls).filter(cls.id == doctor_id).first()

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

def delete_doctor(session, doctor_id):
    try:
        doctor = session.query(Doctor).filter_by(id=doctor_id).first()
        if doctor:
            session.delete(doctor)
            session.commit()
            print("Doctor deleted successfully.")
        else:
            print("Doctor not found.")
    except Exception as e:
        print("Error occurred while deleting doctor:", e)

def update_doctor(session, doctor_id, new_name, new_speciality, new_contact):
    try:
        doctor = session.query(Doctor).filter_by(id=doctor_id).first()
        if doctor:
            doctor.name = new_name
            doctor.speciality = new_speciality
            doctor.contact = new_contact
            session.commit()
            print("Doctor updated successfully.")
        else:
            print("Doctor not found.")
    except Exception as e:
        print("Error occurred while updating doctor:", e)