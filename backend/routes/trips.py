from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models.trip import TripModel
from schemas.trip import Trip, TripResponse

router = APIRouter()

# Dependency (databas-session)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# GET all
@router.get("/trips", response_model=list[TripResponse])
def get_trips(db: Session = Depends(get_db)):
    return db.query(TripModel).all()

# GET one
@router.get("/trips/{trip_id}", response_model=TripResponse)
def get_trip(trip_id: int, db: Session = Depends(get_db)):
    trip = db.query(TripModel).filter(TripModel.id == trip_id).first()
    return trip

# POST
@router.post("/trips", response_model=TripResponse)
def create_trip(trip: Trip, db: Session = Depends(get_db)):
    new_trip = TripModel(destination=trip.destination, status=trip.status)
    db.add(new_trip)
    db.commit()
    db.refresh(new_trip)
    return new_trip

# PUT
@router.put("/trips/{trip_id}", response_model=TripResponse)
def update_trip(trip_id: int, updated_trip: Trip, db: Session = Depends(get_db)):
    trip = db.query(TripModel).filter(TripModel.id == trip_id).first()
    if trip:
        trip.destination = updated_trip.destination
        trip.status = updated_trip.status
        db.commit()
        db.refresh(trip)
    return trip

# DELETE
@router.delete("/trips/{trip_id}")
def delete_trip(trip_id: int, db: Session = Depends(get_db)):
    trip = db.query(TripModel).filter(TripModel.id == trip_id).first()
    if trip:
        db.delete(trip)
        db.commit()
        return {"message": "Deleted"}
    return {"error": "Not found"}