from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import List

# Mount frontend
app.mount("/static", StaticFiles(directory="frontend/assets"), name="static")

# Database model
class Diagnosis(BaseModel):
    doctor_id: str
    patient_id: str
    diagnosis: str
    confidence: float

# Mock database
diagnoses_db: List[Diagnosis] = []

@app.post("/save-diagnosis")
async def save_diagnosis(diagnosis: Diagnosis):
    diagnoses_db.append(diagnosis)
    return {"message": "تم الحفظ بنجاح"}
