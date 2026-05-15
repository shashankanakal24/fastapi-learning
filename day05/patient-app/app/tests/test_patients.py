from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


# CREATE PATIENT TEST

def test_create_patient():

    payload = {
        "id": "P100",
        "name": "John",
        "age": 30,
        "gender": "male",
        "height": 1.75,
        "weight": 70,
        "email": "john@nichi.com",
        "contact": {
            "phone": "9999999999"
        },
        "allergies": [
            "dust"
        ],
        "address": {
            "city": "Chennai",
            "state": "Tamil Nadu",
            "pincode": 600001
        }
    }

    response = client.post(
        "/patients/",
        json=payload
    )

    assert response.status_code == 201

    assert response.json()["success"] is True


# GET ALL PATIENTS TEST

def test_get_all_patients():

    response = client.get("/patients/")

    assert response.status_code == 200

    assert response.json()["success"] is True


# GET PATIENT BY ID TEST

def test_get_patient_by_id():

    response = client.get(
        "/patients/P100"
    )

    assert response.status_code == 200

    data = response.json()

    assert data["success"] is True

    assert data["data"]["id"] == "P100"


# UPDATE PATIENT TEST

def test_update_patient():

    payload = {
        "weight": 80
    }

    response = client.put(
        "/patients/P100",
        json=payload
    )

    assert response.status_code == 200

    data = response.json()

    assert data["success"] is True

    assert data["data"]["weight"] == 80


# DELETE PATIENT TEST

def test_delete_patient():

    response = client.delete(
        "/patients/P100"
    )

    assert response.status_code == 200

    assert response.json()["success"] is True