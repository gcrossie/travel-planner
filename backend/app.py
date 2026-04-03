from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI backend!"}

trips = [
    {"id": 1, "destination": "Paris", "status": "Packing"},
    {"id": 2, "destination": "Tokyo", "status": "Planned"}
]

@app.get("/trips")
def get_trips():
    return trips

from pydantic import BaseModel

# Schema (struktur för data)
class Trip(BaseModel):
    destination: str
    status: str

# POST endpoint
@app.post("/trips")
def create_trip(trip: Trip):
    new_trip = {
        "id": len(trips) + 1,
        "destination": trip.destination,
        "status": trip.status
    }
    trips.append(new_trip)
    return new_trip

@app.get("/trips/{trip_id}")
def get_trip(trip_id: int):
    for trip in trips:
        if trip["id"] == trip_id:
            return trip
    return {"error": "Trip not found"}

@app.delete("/trips/{trip_id}")
def delete_trip(trip_id: int):
    for trip in trips:
        if trip["id"] == trip_id:
            trips.remove(trip)
            return {"message": "Trip deleted"}
    
    return {"error": "Trip not found"}

@app.put("/trips/{trip_id}")
def update_trip(trip_id: int, updated_trip: Trip):
    for trip in trips:
        if trip["id"] == trip_id:
            trip["destination"] = updated_trip.destination
            trip["status"] = updated_trip.status
            return trip

    return {"error": "Trip not found"}
