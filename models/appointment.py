from sqlalchemy import Column, Integer, String, ForeignKey
from database.connection import Base

class Appointment(Base):
    __tablename__ = 'appointment'

    id = Column(Integer, primary_key=True, index=True)
    appointment_date = Column(String, nullable=False)
    reason = Column(String, nullable=False)
    status = Column(String, nullable=False)
    patient_id = Column(Integer, ForeignKey('patient.id'))
    doctor_id = Column(Integer, ForeignKey('doctor.id'))

    @classmethod
    def find_by_id(cls, session, appointment_id):
        return session.query(cls).filter(cls.id == appointment_id).first()

def create_appointment(session, appointment_data: dict):
    try:
        appointment = Appointment(**appointment_data)
        session.add(appointment)
        session.commit()
        print("Appointment created successfully.")
    except Exception as e:
        print("Error occurred while creating appointment:", e)

def list_appointments(session):
    try:
        appointments = session.query(Appointment).all()
        if appointments:
            print("Appointments:")
            for appointment in appointments:
                appointment_data = {
                    "ID": appointment.id,
                    "Date": appointment.appointment_date,
                    "Reason": appointment.reason,
                    "Status": appointment.status,
                    "Patient ID": appointment.patient_id,
                    "Doctor ID": appointment.doctor_id
                }
                print(appointment_data)
        else:
            print("No appointments found.")
    except Exception as e:
        print("Error occurred while listing appointments:", e)

def delete_appointment(session, appointment_id):
    try:
        appointment = session.query(Appointment).filter_by(id=appointment_id).first()
        if appointment:
            session.delete(appointment)
            session.commit()
            print("Appointment deleted successfully.")
        else:
            print("Appointment not found.")
    except Exception as e:
        print("Error occurred while deleting appointment:", e)

def update_appointment(session, appointment_id, update_data: dict):
    try:
        appointment = session.query(Appointment).filter_by(id=appointment_id).first()
        if appointment:
            for key, value in update_data.items():
                setattr(appointment, key, value)
            session.commit()
            print("Appointment updated successfully.")
        else:
            print("Appointment not found.")
    except Exception as e:
        print("Error occurred while updating appointment:", e)

# Example usage
if __name__ == "__main__":
    from sqlalchemy.orm import sessionmaker
    from database.connection import engine

    Session = sessionmaker(bind=engine)
    session = Session()

    # Create an appointment
    appointment_data = {
        "appointment_date": "2024-06-15",
        "reason": "Routine check-up",
        "status": "Scheduled",
        "patient_id": 1,
        "doctor_id": 2
    }
    create_appointment(session, appointment_data)

    # List all appointments
    list_appointments(session)

    # Update an appointment
    update_data = {
        "appointment_date": "2024-06-16",
        "reason": "Follow-up",
        "status": "Confirmed",
        "patient_id": 1,
        "doctor_id": 2
    }
    update_appointment(session, appointment_id=1, update_data=update_data)

    # Delete an appointment
    delete_appointment(session, appointment_id=1)
