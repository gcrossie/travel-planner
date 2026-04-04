# Travel Planner
Gabriella Cross

## Beskrivning
Detta är en fullstack CRUD-applikation där användaren kan planera en resa genom att lägga till olika typer av aktiviteter såsom flights, hotels, activities, restaurants och hidden gems.

Applikationen låter användaren:
- Skapa nya poster
- Visa alla poster
- Uppdatera poster
- Ta bort poster

## Tech stack
- Backend: FastAPI
- Frontend: React (Vite)
- Databas: SQLite

## Starta backend
cd backend  
pip install -r requirements.txt  
uvicorn app:app --reload  

Backend körs på:  
http://127.0.0.1:8000  

API docs:  
http://127.0.0.1:8000/docs  

## Starta frontend
cd frontend  
npm install  
npm run dev  

Frontend körs på:  
http://localhost:5173  

## Endpoints
- POST /trips  
- GET /trips  
- GET /trips/{id}  
- PUT /trips/{id}  
- DELETE /trips/{id}