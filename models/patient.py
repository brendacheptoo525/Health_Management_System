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

    @classmethod
    def find_by_id(cls, session, patient_id):
        return session.query(cls).filter(cls.id == patient_id).first()
        
def create_patient(session, patient_data: dict):
    try:
        patient = Patient(**patient_data)
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
                patient_data = {
                    "ID": patient.id,
                    "Name": patient.name,
                    "Age": patient.age,
                    "Illness": patient.illness,
                    "Doctor ID": patient.doctor_id
                }
                print(patient_data)
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

def update_patient(session, patient_id, update_data: dict):
    try:
        patient = session.query(Patient).filter_by(id=patient_id).first()
        if patient:
            for key, value in update_data.items():
                setattr(patient, key, value)
            session.commit()
            print("Patient updated successfully.")
        else:
            print("Patient not found.")
    except Exception as e:
        print("Error occurred while updating patient:", e)

# Example usage
if __name__ == "__main__":
    from sqlalchemy.orm import sessionmaker
    from database.connection import engine

    Session = sessionmaker(bind=engine)
    session = Session()

    # Create a patient
    patient_data = {
        "name": "Jane Doe",
        "age": 30,
        "illness": "Flu",
        "doctor_id": 1
    }
    create_patient(session, patient_data)

    # List all patients
    list_patients(session)

    # Update a patient
    update_data = {
        "name": "Jane Smith",
        "age": 31,
        "illness": "Cold",
        "doctor_id": 2
    }
    update_patient(session, patient_id=1, update_data=update_data)

    # Delete a patient
    delete_patient(session, patient_id=1)
