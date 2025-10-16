from fastapi import FastAPI, Response, status
import requests
from datetime import datetime, timezone

EMAIL = "zinsusezonsu@gmail.com"
NAME = "Zinsu Sezonsu"
STACK = "FastApi" 
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
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
    
    

app = FastAPI()

@app.get("/")
def welcome_message():
    welcome_msg = {"message": "Welcome to Zinsu Backend Wizards  Stage 0",
                   "info": "visit /me to view my profile with a random cat fact"}
    return welcome_msg
@app.get("/me")
def get_profile():
    res = cat_fact() 
    time = current_utc_time()
    data = {"status": "success",
            "email": EMAIL,
            "name": NAME,
            "Stack": STACK,
            "fact": res,
            "timestaps": time}

    return data