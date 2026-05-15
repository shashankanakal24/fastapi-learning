from sqlalchemy.orm import Session

from .model import Patient


def create_patient(
    db: Session,
    payload
):

    patient = Patient(**payload)

    db.add(patient)

    db.commit()

    db.refresh(patient)

    return patient


def get_patient_by_id(
    db: Session,
    patient_id: str
):

    return db.query(Patient).filter(
        Patient.id == patient_id
    ).first()


def get_all_patients(
    db: Session
):

    return db.query(Patient).all()


def update_patient(
    db: Session,
    patient,
    payload
):

    for key, value in payload.items():

        setattr(patient, key, value)

    db.commit()

    db.refresh(patient)

    return patient


def delete_patient(
    db: Session,
    patient
):

    db.delete(patient)

    db.commit()