from sqlalchemy import create_engine
from database.connection import Base, DATABASE_URL
from models.patient import Patient
from models.doctor import Doctor
from models.appointment import Appointment