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

def create_appointment(session, appointment_date, reason, status, patient_id, doctor_id):
    try:
        appointment = Appointment(appointment_date=appointment_date, reason=reason, status=status, patient_id=patient_id, doctor_id=doctor_id)
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
                print(f"ID: {appointment.id}, Date: {appointment.appointment_date}, Reason: {appointment.reason}, Status: {appointment.status}, Patient ID: {appointment.patient_id}, Doctor ID: {appointment.doctor_id}")
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

def update_appointment(session, appointment_id, new_date, new_reason, new_status, new_patient_id, new_doctor_id):
    try:
        appointment = session.query(Appointment).filter_by(id=appointment_id).first()
        if appointment:
            appointment.appointment_date = new_date
            appointment.reason = new_reason
            appointment.status = new_status
            appointment.patient_id = new_patient_id
            appointment.doctor_id = new_doctor_id
            session.commit()
            print("Appointment updated successfully.")
        else:
            print("Appointment not found.")
    except Exception as e:
        print("Error occurred while updating appointment:", e)