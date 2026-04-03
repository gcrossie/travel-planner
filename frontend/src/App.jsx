import { useEffect, useState } from "react";

function App() {
  const [trips, setTrips] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/trips")
      .then((res) => res.json())
      .then((data) => setTrips(data))
      .catch((err) => console.error(err));
  }, []);

  return (
    <div style={{ padding: "20px" }}>
      <h1>Travel Planner ✈️</h1>

      {trips.length === 0 ? (
        <p>No trips yet...</p>
      ) : (
        trips.map((trip) => (
          <div key={trip.id}>
            <h2>{trip.title}</h2>
            <p>{trip.category}</p>
            <p>{trip.date}</p>
            <p>{trip.status}</p>
            <p>{trip.notes}</p>
          </div>
        ))
      )}
    </div>
  );
}

export default App;