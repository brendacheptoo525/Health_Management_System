from sqlalchemy.orm import sessionmaker
from database.connection import create_engine, DATABASE_URL
from models.patient import create_patient, update_patient, delete_patient, list_patients
from models.doctor import create_doctor, update_doctor, delete_doctor, list_doctors
from models.appointment import create_appointment, update_appointment, delete_appointment, list_appointments

# Create engine and session
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
