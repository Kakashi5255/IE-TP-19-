# routers/parking.py

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from db import get_db
from models import ParkingStatus
from typing import Optional

router = APIRouter()

@router.get("/api/parking")
def get_parking_status(
    zone_number: Optional[int] = Query(None),
    status_description: Optional[str] = Query(None),
    db: Session = Depends(get_db)
):
    query = db.query(ParkingStatus)

    if zone_number is not None:
        query = query.filter(ParkingStatus.zone_number == zone_number)
    
    if status_description is not None:
        query = query.filter(ParkingStatus.status_description.ilike(status_description.strip()))

    results = query.all()

    if not results:
        return {"message": "No parking records found for the given filters."}

    return [
        {
            "lastupdated": r.lastupdated,
            "status_timestamp": r.status_timestamp,
            "zone_number": r.zone_number,
            "status_description": r.status_description,
            "kerbsideid": r.kerbsideid,
            "location": r.location
        }
        for r in results
    ]
