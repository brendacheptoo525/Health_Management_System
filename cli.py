from sqlalchemy.orm import sessionmaker
from database.connection import create_engine, DATABASE_URL
from models.patient import Patient, create_patient, update_patient, delete_patient, list_patients
from models.doctor import Doctor, create_doctor, update_doctor, delete_doctor, list_doctors
from models.appointment import Appointment, create_appointment, update_appointment, delete_appointment, list_appointments

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
            print("13. Find Patient by ID")
            print("14. Find Doctor by ID")
            print("15. Find Appointment by ID")
            print("16. Exit")
     
            choice = input("Enter your choice: ")
     
            if choice == '1':
                name = input("Enter patient name: ")
                age = int(input("Enter patient age: "))
                illness = input("Enter patient illness: ")
                doctor_id = int(input("Enter doctor id: "))
                patient_data = {
                    "name": name,
                    "age": age,
                    "illness": illness,
                    "doctor_id": doctor_id
                }
                create_patient(session, patient_data)
            elif choice == '2':
                name = input("Enter doctor name: ")
                speciality = input("Enter doctor speciality: ")
                contact = input("Enter doctor contact: ")
                doctor_data = {
                    "name": name,
                    "speciality": speciality,
                    "contact": contact
                }
                create_doctor(session, doctor_data)
            elif choice == '3':
                appointment_date = input("Enter appointment date (YYYY-MM-DD): ")
                reason = input("Enter appointment reason: ")
                status = input("Enter appointment status: ")
                patient_id = int(input("Enter patient id: "))
                doctor_id = int(input("Enter doctor id: "))
                appointment_data = {
                    "appointment_date": appointment_date,
                    "reason": reason,
                    "status": status,
                    "patient_id": patient_id,
                    "doctor_id": doctor_id
                }
                create_appointment(session, appointment_data)
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
                update_data = {
                    "name": new_name,
                    "age": new_age,
                    "illness": new_illness,
                    "doctor_id": new_doctor_id
                }
                update_patient(session, patient_id, update_data)
            elif choice == '8':
                doctor_id = int(input("Enter doctor id to update: "))
                new_name = input("Enter new doctor name: ")
                new_speciality = input("Enter new doctor speciality: ")
                new_contact = input("Enter new doctor contact: ")
                update_data = {
                    "name": new_name,
                    "speciality": new_speciality,
                    "contact": new_contact
                }
                update_doctor(session, doctor_id, update_data)
            elif choice == '9':
                appointment_id = int(input("Enter appointment id to update: "))
                new_date = input("Enter new appointment date (YYYY-MM-DD): ")
                new_reason = input("Enter new appointment reason: ")
                new_status = input("Enter new appointment status: ")
                new_patient_id = int(input("Enter new patient id: "))
                new_doctor_id = int(input("Enter new doctor id: "))
                update_data = {
                    "appointment_date": new_date,
                    "reason": new_reason,
                    "status": new_status,
                    "patient_id": new_patient_id,
                    "doctor_id": new_doctor_id
                }
                update_appointment(session, appointment_id, update_data)
            elif choice == '10':
                patient_id = int(input("Enter patient id to delete: "))
                delete_patient(session, patient_id)
            elif choice == '11':
                doctor_id = int(input("Enter doctor id to delete: "))
                delete_doctor(session, doctor_id)
            elif choice == '12':
                appointment_id = int(input("Enter appointment id to delete: "))
                delete_appointment(session, appointment_id)
            elif choice == '13':
                patient_id = int(input("Enter patient ID to find: "))
                patient = Patient.find_by_id(session, patient_id)
                if patient:
                    print("Patient found:")
                    print(f"ID: {patient.id}, Name: {patient.name}, Age: {patient.age}, Illness: {patient.illness}, Doctor ID: {patient.doctor_id}")
                else:
                    print("Patient not found.")
            elif choice == '14':
                doctor_id = int(input("Enter doctor ID to find: "))
                doctor = Doctor.find_by_id(session, doctor_id)
                if doctor:
                    print("Doctor found:")
                    print(f"ID: {doctor.id}, Name: {doctor.name}, Speciality: {doctor.speciality}, Contact: {doctor.contact}")
                else:
                    print("Doctor not found.")
            elif choice == '15':
                appointment_id = int(input("Enter appointment ID to find: "))
                appointment = Appointment.find_by_id(session, appointment_id)
                if appointment:
                    print("Appointment found:")
                    print(f"ID: {appointment.id}, Date: {appointment.appointment_date}, Reason: {appointment.reason}, Status: {appointment.status}, Patient ID: {appointment.patient_id}, Doctor ID: {appointment.doctor_id}")
                else:
                    print("Appointment not found.")
            elif choice == '16':
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please try again.")
    finally:
        session.close()

if __name__ == '__main__':
    menu()
