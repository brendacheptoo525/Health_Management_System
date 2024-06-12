from sqlalchemy import Column, Integer, String, ForeignKey
from database.connection import Base

class Appointment(Base):
    _tablename_ = 'appointment'

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
