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

def create_doctor(session, doctor_data: dict):
    try:
        doctor = Doctor(**doctor_data)
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
                doctor_data = {
                    "ID": doctor.id,
                    "Name": doctor.name,
                    "Specialty": doctor.specialty,
                    "Contact": doctor.contact
                }
                print(doctor_data)
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

def update_doctor(session, doctor_id, update_data: dict):
    try:
        doctor = session.query(Doctor).filter_by(id=doctor_id).first()
        if doctor:
            for key, value in update_data.items():
                setattr(doctor, key, value)
            session.commit()
            print("Doctor updated successfully.")
        else:
            print("Doctor not found.")
    except Exception as e:
        print("Error occurred while updating doctor:", e)

# Example usage
if __name__ == "__main__":
    from sqlalchemy.orm import sessionmaker
    from database.connection import engine

    Session = sessionmaker(bind=engine)
    session = Session()

    # Create a doctor
    doctor_data = {
        "name": "Dr. John Doe",
        "specialty": "Cardiology",
        "contact": "123-456-7890"
    }
    create_doctor(session, doctor_data)

    # List all doctors
    list_doctors(session)

    # Update a doctor
    update_data = {
        "name": "Dr. John Smith",
        "specialty": "Neurology",
        "contact": "098-765-4321"
    }
    update_doctor(session, doctor_id=1, update_data=update_data)

    # Delete a doctor
    delete_doctor(session, doctor_id=1)
