import pandas as pd
from sqlalchemy.orm import Session
from db import SessionLocal
from models import ParkingStatus, VehicleRegistration, Base
from db import engine

# ---------------------- EPIC 1: Upload to Supabase ----------------------
Base.metadata.create_all(bind=engine)
df = pd.read_csv("epic1_dataset.csv")
df.columns = df.columns.str.strip().str.lower()  

db: Session = SessionLocal()

for _, row in df.iterrows():
    record = VehicleRegistration(
        state=row["state"],
        year_range=row["year range"],
        total=int(row["total"]),
        percentage=float(row["percentage"])
    )
    db.add(record)

db.commit()
db.close()

# ---------------------- EPIC 2: Function to Load into Memory ----------------------
df = pd.read_csv("epic2_dataset.csv")
df.columns = df.columns.str.strip().str.lower()

db: Session = SessionLocal()

for _, row in df.iterrows():
    record = ParkingStatus(
        lastupdated=row["lastupdated"],
        status_timestamp=row["status_timestamp"],
        zone_number=int(row["zone_number"]) if pd.notna(row["zone_number"]) else None,
        status_description=row["status_description"],
        kerbsideid=int(row["kerbsideid"]) if pd.notna(row["kerbsideid"]) else None,
        location=row["location"]
    )
    db.add(record)

db.commit()
db.close()

