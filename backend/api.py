from fastapi import FastAPI
from scheduler import generate_schedule  # we will adjust if name differs

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Backend is running 🚀"}

@app.post("/schedule")
def get_schedule(topics: list[str]):
    result = generate_schedule(topics)
    return {"schedule": result}
