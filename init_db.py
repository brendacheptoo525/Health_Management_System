from sqlalchemy import create_engine
from database.connection import Base, DATABASE_URL
from models.patient import Patient
from models.doctor import Doctor
from models.appointment import Appointment

def init_db():
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(bind=engine)

if _name_ == '_main_':
    init_db()