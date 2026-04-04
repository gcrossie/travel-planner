# Travel Planner

## Description
This is a fullstack CRUD application where users can plan trips by adding different types of items such as flights, hotels, activities, restaurants, and hidden gems.

The application allows users to:
- Create new trips
- View all trips
- Update trips
- Delete trips

## Tech Stack
- Backend: FastAPI
- Frontend: React (Vite)
- Database: SQLite

## Run the Backend
cd backend  
pip install -r requirements.txt  
uvicorn app:app --reload  

Backend runs on:  
http://127.0.0.1:8000  

API docs:  
http://127.0.0.1:8000/docs  

## Run the Frontend
cd frontend  
npm install  
npm run dev  

Frontend runs on:  
http://localhost:5173  

## API Endpoints
- POST /trips  
- GET /trips  
- GET /trips/{id}  
- PUT /trips/{id}  
- DELETE /trips/{id}