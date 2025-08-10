from fastapi import FastAPI
from routers import car_ownership, parking
import models
from db import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(car_ownership.router)


@app.get("/healthz")
def health_check():
    return {"status": "ok"}