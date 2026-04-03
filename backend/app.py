from fastapi import FastAPI
from database import engine, Base
from routes.trips import router as trips_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI backend!"}

app.include_router(trips_router)