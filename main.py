from fastapi import FastAPI
import requests
from datetime import datetime, timezone

EMAIL = "zinsusezonsu@gmail.com"
NAME = "Zinsu Sezonsu Emmanuel"
STACK = "Python (FastAPI)"
CAT_API = "https://catfact.ninja/fact"

def cat_fact():
    try:
        response = requests.get(CAT_API, timeout=5)
        response.raise_for_status()
        data = response.json()
        return data.get("fact", "No cat fact available")
    except requests.Timeout:
        return "Could not fetch a cat fact at this time. Timeout"
    except requests.ConnectionError:
        return "Could not fetch a cat fact at this time. Connection Failed"
    except requests.RequestException as e:
        return f"An error occurred while fetching the cat fact: {str(e)}"

def current_utc_time():
    # Correct ISO 8601 format (with 'Z' at the end)
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")

app = FastAPI()

@app.get("/")
def welcome_message():
    return {
        "message": "Welcome to Zinsu Backend Wizards Stage 0",
        "info": "Visit /me to view my profile with a random cat fact"
    }

@app.get("/me")
def get_profile():
    res = cat_fact()
    time = current_utc_time()
    data = {
        "status": "success",
        "user": {
            "email": EMAIL,
            "name": NAME,
            "stack": STACK
        },
        "timestamp": time,
        "fact": res
    }
    return data
