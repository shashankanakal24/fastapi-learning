from app.core.database import Base, engine

from app.modules.patients.model import Patient

Base.metadata.create_all(bind=engine)