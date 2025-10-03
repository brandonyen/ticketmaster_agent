from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import httpx
from dotenv import load_dotenv
import os

load_dotenv()
app = FastAPI()

TICKETMASTER_API_KEY = os.environ.get('TICKETMASTER_API_KEY')

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TicketmasterEvent(BaseModel):
    name: str

class TicketmasterEvents(BaseModel):
    events: List[TicketmasterEvent]

class TicketmasterResponse(BaseModel):
    _embedded: TicketmasterEvents
    
@app.get('/api/v1/chat')
async def fetch_events(city: str, keyword=""):
    ticketmaster_query_url = f"https://app.ticketmaster.com/discovery/v2/events.json?apikey={TICKETMASTER_API_KEY}&city={city}&keyword={keyword}&size=5&page=1"
    try:
        async with httpx.AsyncClient() as client:
            event_response = await client.get(ticketmaster_query_url)
            event_response.raise_for_status()

            if not event_response.json().get('_embedded'):
                raise HTTPException(status_code=404, detail="No events in the given city.")
            
            events: TicketmasterResponse = event_response.json()

            return events
    
    except httpx.HTTPError as exc:
        raise HTTPException(status_code=503, detail=f"External API request failed: {str(exc)}")
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(exc)}")