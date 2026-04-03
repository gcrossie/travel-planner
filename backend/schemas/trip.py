from pydantic import BaseModel

class Trip(BaseModel):
    title: str
    category: str
    date: str
    status: str
    notes: str

class TripResponse(Trip):
    id: int

    class Config:
        from_attributes = True