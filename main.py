from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import car_ownership
import models
from db import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Enable CORS for all domains (change "*" to specific domains for production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers (Epic 1 only)
app.include_router(car_ownership.router)

@app.get("/healthz")
def health_check():
    return {"status": "ok"}
