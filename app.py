from fastapi import FastAPI
from pydantic import BaseModel
from agent import agent

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Travel AI API Running"}

class TravelRequest(BaseModel):
    query: str

@app.post("/travel-assistant")
async def travel_assistant(request: TravelRequest):

    try:
        response = agent.invoke(request.query)

        return {
            "response": response.content
        }

    except Exception as e:
        return {
            "error": str(e)
        }