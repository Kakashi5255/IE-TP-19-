# routers/parking.py

from fastapi import APIRouter

router = APIRouter()

@router.get("/api/parking")
def dummy_parking_endpoint():
    return {"message": "Parking endpoint is working!"}
