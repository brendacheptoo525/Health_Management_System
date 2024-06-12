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

