from fastapi import (
    APIRouter,
    Depends
)

from sqlalchemy.orm import Session

from app.core.dependencies import get_db

from .schema import (
    PatientCreate,
    PatientUpdate
)

from .service import (
    create_patient_service,
    get_patient_service,
    get_all_patients_service,
    update_patient_service,
    delete_patient_service
)

from app.common.helpers.response import (
    success_response
)

router = APIRouter(
    prefix="/patients",
    tags=["Patients"]
)


@router.post("/")

def create_patient_api(
    payload: PatientCreate,
    db: Session = Depends(get_db)
):

    patient = create_patient_service(
        db,
        payload
    )

    return success_response(
        "Patient created successfully",
        patient.id,
        201
    )


@router.get("/")

def get_all_patients_api(
    db: Session = Depends(get_db)
):

    patients = get_all_patients_service(db)

    patient_list = []

    for patient in patients:

        patient_list.append({

            "id": patient.id,
            "name": patient.name,
            "age": patient.age,
            "gender": patient.gender,
            "height": patient.height,
            "weight": patient.weight,
            "email": patient.email,
            "contact": patient.contact,
            "allergies": patient.allergies,
            "address": patient.address

        })

    return success_response(
        "Patients fetched successfully",
        patient_list
    )

@router.get("/{patient_id}")

def get_patient_api(
    patient_id: str,
    db: Session = Depends(get_db)
):

    patient = get_patient_service(
        db,
        patient_id
    )

    # return success_response(
    #     "Patient fetched successfully",
    #     patient
    # )
    
    return success_response(
    "Patient fetched successfully",
    {
        "id": patient.id,
        "name": patient.name,
        "age": patient.age,
        "gender": patient.gender,
        "height": patient.height,
        "weight": patient.weight,
        "email": patient.email,
        "contact": patient.contact,
        "allergies": patient.allergies,
        "address": patient.address
    }
)


@router.put("/{patient_id}")

def update_patient_api(
    patient_id: str,
    payload: PatientUpdate,
    db: Session = Depends(get_db)
):

    patient = update_patient_service(
        db,
        patient_id,
        payload
    )

    # return success_response(
    #     "Patient updated successfully",
    #     patient
    # )
    
    return success_response(
    "Patient updated successfully",
    {
        "id": patient.id,
        "name": patient.name,
        "age": patient.age,
        "gender": patient.gender,
        "height": patient.height,
        "weight": patient.weight,
        "email": patient.email,
        "contact": patient.contact,
        "allergies": patient.allergies,
        "address": patient.address
    }
)


@router.delete("/{patient_id}")

def delete_patient_api(
    patient_id: str,
    db: Session = Depends(get_db)
):

    delete_patient_service(
        db,
        patient_id
    )

    return success_response(
        "Patient deleted successfully"
    )