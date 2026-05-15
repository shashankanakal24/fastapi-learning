from fastapi import HTTPException

from .repository import (
    create_patient,
    get_patient_by_id,
    get_all_patients,
    update_patient,
    delete_patient
)


def create_patient_service(
    db,
    payload
):

    existing = get_patient_by_id(
        db,
        payload.id
    )

    if existing:
        raise HTTPException(
            status_code=400,
            detail="Patient already exists"
        )

    return create_patient(
        db,
        payload.model_dump(
            exclude_computed_fields=True
        )
    )


def get_patient_service(
    db,
    patient_id
):

    patient = get_patient_by_id(
        db,
        patient_id
    )

    if not patient:
        raise HTTPException(
            status_code=404,
            detail="Patient not found"
        )

    return patient


def get_all_patients_service(db):

    return get_all_patients(db)


def update_patient_service(
    db,
    patient_id,
    payload
):

    patient = get_patient_by_id(
        db,
        patient_id
    )

    if not patient:
        raise HTTPException(
            status_code=404,
            detail="Patient not found"
        )

    updated_data = payload.model_dump(
        exclude_unset=True
    )

    return update_patient(
        db,
        patient,
        updated_data
    )


def delete_patient_service(
    db,
    patient_id
):

    patient = get_patient_by_id(
        db,
        patient_id
    )

    if not patient:
        raise HTTPException(
            status_code=404,
            detail="Patient not found"
        )

    delete_patient(
        db,
        patient
    )