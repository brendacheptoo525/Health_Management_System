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

            if choice == '1':
                name = input("Enter patient name: ")
                age = int(input("Enter patient age: "))
                illness = input("Enter patient illness: ")
                doctor_id = int(input("Enter doctor id: "))
                create_patient(session, name, age, illness, doctor_id)
            elif choice == '2':
                name = input("Enter doctor name: ")
                speciality = input("Enter doctor speciality: ")
                contact = input("Enter doctor contact: ")
                create_doctor(session, name, speciality, contact)
            elif choice == '3':
                appointment_date = input("Enter appointment date (YYYY-MM-DD): ")
                reason = input("Enter appointment reason: ")
                status = input("Enter appointment status: ")
                patient_id = int(input("Enter patient id: "))
                doctor_id = int(input("Enter doctor id: "))
                create_appointment(session, appointment_date, reason, status, patient_id, doctor_id)
            
            elif choice == '4':
                list_patients(session)
            elif choice == '5':
                list_doctors(session)
            elif choice == '6':
                list_appointments(session)

            elif choice == '7':
                patient_id = int(input("Enter patient id to update: "))
                new_name = input("Enter new patient name: ")
                new_age = int(input("Enter new patient age: "))
                new_illness = input("Enter new patient illness: ")
                new_doctor_id = int(input("Enter new doctor id: "))
                update_patient(session, patient_id, new_name, new_age, new_illness, new_doctor_id)
            elif choice == '8':
                doctor_id = int(input("Enter doctor id to update: "))
                new_name = input("Enter new doctor name: ")
                new_speciality = input("Enter new doctor speciality: ")
                new_contact = input("Enter new doctor contact: ")
                update_doctor(session, doctor_id, new_name, new_speciality, new_contact)
            elif choice == '9':
                appointment_id = int(input("Enter appointment id to update: "))
                new_date = input("Enter new appointment date (YYYY-MM-DD): ")
                new_reason = input("Enter new appointment reason: ")
                new_status = input("Enter new appointment status: ")
                new_patient_id = int(input("Enter new patient id: "))
                new_doctor_id = int(input("Enter new doctor id: "))
                update_appointment(session, appointment_id, new_date, new_reason, new_status, new_patient_id, new_doctor_id)

