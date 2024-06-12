from sqlalchemy.orm import sessionmaker
from database.connection import create_engine, DATABASE_URL
from models.patient import create_patient, update_patient, delete_patient, list_patients
from models.doctor import create_doctor, update_doctor, delete_doctor, list_doctors
from models.appointment import create_appointment, update_appointment, delete_appointment, list_appointments

# Create engine and session
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def menu():
    session = SessionLocal()  # Correct instantiation of session
    try:
        while True:
            print("\nMenu:")
            print("1. Create Patient")
            print("2. Create Doctor")
            print("3. Create Appointment")
            print("4. List Patients")
            print("5. List Doctors")
            print("6. List Appointments")
            print("7. Update Patient")
            print("8. Update Doctor")
            print("9. Update Appointment")
            print("10. Delete Patient")
            print("11. Delete Doctor")
            print("12. Delete Appointment")
            print("13. Exit")

            