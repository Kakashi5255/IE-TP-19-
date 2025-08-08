from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from db import get_db
from models import VehicleRegistration
from typing import Optional

router = APIRouter()

@router.get("/api/car-ownership")
def get_car_ownership(
    state: Optional[str] = Query(None),
    year_range: Optional[str] = Query(None),
    db: Session = Depends(get_db)
):
    query = db.query(VehicleRegistration)

    if state:
        query = query.filter(VehicleRegistration.state.ilike(state.strip()))
    if year_range:
        query = query.filter(VehicleRegistration.year_range == year_range.strip())

    results = query.all()

    if not results:
        return {"message": "No records found for the given filters."}

    return [
        {
            "state": record.state,
            "year_range": record.year_range,
            "total": record.total,
            "percentage": record.percentage
        }
        for record in results
    ]
