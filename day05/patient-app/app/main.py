from fastapi import FastAPI

from app.modules.patients.router import router as patient_router

app = FastAPI()

app.include_router(patient_router)