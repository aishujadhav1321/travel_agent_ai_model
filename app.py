from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Travel AI API Running"}

class TravelRequest(BaseModel):
    query: str

@app.post("/travel-assistant")
async def travel_assistant(request: TravelRequest):
    return {
        "response": "test working"
    }