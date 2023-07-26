import bcrypt
from sqlalchemy import Column, Integer, String, DateTime, Boolean, Text, Float
from sqlalchemy.orm import relationship
from datetime import datetime

from app.config.database import Base


class Person(Base):
    __tablename__ = "person"

    id = Column(Integer, primary_key=True, autoincrement=True)
    surname = Column(String(100), nullable=False)
    name = Column(String(100), nullable=False)
    identification_number = Column(String(100), nullable=False)
    birthdate = Column(DateTime, nullable=False)
    id_gender = Column(Integer, nullable=False, default=1)
    id_department = Column(Integer, nullable=False, default=1)
    id_locality = Column(Integer, nullable=True, default=1)
    address_street = Column(String(250), nullable=False, default="")
    address_number = Column(String(100), nullable=False, default="")
    id_usual_institution = Column(Integer, nullable=False)
    is_diabetic = Column(Boolean, nullable=False, default=0)
    is_hypertensive = Column(Boolean, nullable=False, default=0)
    is_chronic_respiratory_disease = Column(Boolean, nullable=False, default=0)
    is_chronic_kidney_disease = Column(Boolean, nullable=False, default=0)
    identification_number_master = Column(String(100), nullable=False)
    id_identification_type = Column(Integer, nullable=True)
    id_identification_type_master = Column(Integer, nullable=True)
    is_deleted = Column(Boolean, nullable=True)
    id_patient = Column(Integer, nullable=True)
    id_admin_status = Column(Integer, nullable=True)
    phone_number = Column(String(100), nullable=False)
    department = Column(String(200), nullable=False)
    locality = Column(String(200), nullable=False)
    email = Column(String(200), nullable=False)
    identification_front_image = Column(Text, nullable=True)
    identification_back_image = Column(Text, nullable=True)
    identification_front_image_file_type = Column(String(45), nullable=True)
    identification_back_image_file_type = Column(String(45), nullable=True)
    id_person_status = Column(Integer, nullable=False)
    lat = Column(Float, nullable=True)
    long = Column(Float, nullable=True)
    inst_from_portal = Column(Boolean, nullable=True)

    def __init__(
        self, id: int, surname: str, name: str, identification_number: str, birthdate: datetime, id_gender: int,
            id_department: int, id_locality: int, address_street: str, address_number: str, id_usual_institution: int,
            is_diabetic: bool, is_hypertensive: bool, is_chronic_respiratory_disease: bool,
            is_chronic_kidney_disease: bool, identification_number_master: str, id_identification_type: int,
            id_identification_type_master: int, is_deleted: bool, id_patient: int, id_admin_status: int,
            phone_number: str, department: str, locality: str, email: str, id_person_status: int,
            inst_from_portal: bool, *args, **kargs):
        self.id = id
        self.surname = surname
        self.name = name
        self.identification_number = identification_number
        self.birthdate = birthdate
        self.id_gender = id_gender
        self.id_department = id_department
        self.id_locality = id_locality
        self.address_street = address_street
        self.address_number = address_number
        self.id_usual_institution = id_usual_institution
        self.is_diabetic = is_diabetic
        self.is_hypertensive = is_hypertensive
        self.is_chronic_respiratory_disease = is_chronic_respiratory_disease
        self.is_chronic_kidney_disease = is_chronic_kidney_disease
        self.identification_number_master = identification_number_master
        self.id_identification_type = id_identification_type
        self.id_identification_type_master = id_identification_type_master
        self.is_deleted = is_deleted
        self.id_patient = id_patient
        self.id_admin_status = id_admin_status
        self.phone_number = phone_number
        self.department = department
        self.locality = locality
        self.email = email
        self.id_person_status = id_person_status
        self.inst_from_portal = inst_from_portal
