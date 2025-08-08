import pandas as pd
from sqlalchemy.orm import Session
from db import SessionLocal
from models import VehicleRegistration, Base
from db import engine

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

print(" Data uploaded successfully.")
