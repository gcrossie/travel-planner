from pydantic import BaseModel

class Trip(BaseModel):
    destination: str
    status: str

class TripResponse(Trip):
    id: int

    class Config:
        from_attributes = True