from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database.connection import Base

class Patient(Base):
    __tablename__ = "patient"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    age = Column(Integer)
    illness = Column(String)
    doctor_id = Column(Integer, ForeignKey('doctor.id'))

    doctor = relationship("Doctor", back_populates="patients")

def create_patient(session, name, age, illness, doctor_id):
    try:
        patient = Patient(name=name, age=age, illness=illness, doctor_id=doctor_id)
        session.add(patient)
        session.commit()
        print("Patient created successfully.")
    except Exception as e:
        print("Error occurred while creating patient:", e)

def list_patients(session):
    try:
        patients = session.query(Patient).all()
        if patients:
            print("Patients:")
            for patient in patients:
                print(f"ID: {patient.id}, Name: {patient.name}, Age: {patient.age}, Illness: {patient.illness}, Doctor ID: {patient.doctor_id}")
        else:
            print("No patients found.")
    except Exception as e:
        print("Error occurred while listing patients:", e)

def delete_patient(session, patient_id):
    try:
        patient = session.query(Patient).filter_by(id=patient_id).first()
        if patient:
            session.delete(patient)
            session.commit()
            print("Patient deleted successfully.")
        else:
            print("Patient not found.")
    except Exception as e:
        print("Error occurred while deleting patient:", e)

def update_patient(session, patient_id, new_name, new_age, new_illness, new_doctor_id):
    try:
        patient = session.query(Patient).filter_by(id=patient_id).first()
        if patient:
            patient.name = new_name
            patient.age = new_age
            patient.illness = new_illness
            patient.doctor_id = new_doctor_id
            session.commit()
            print("Patient updated successfully.")
        else:
            print("Patient not found.")
    except Exception as e:
        print("Error occurred while updating patient:", e)