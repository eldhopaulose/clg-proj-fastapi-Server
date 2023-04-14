from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import weather as wr
import pandas as pd
import requests

app = FastAPI()
origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:8000", 
    "http://0.0.0.0:8000",
    "http://127.0.0.1:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    df = pd.read_csv('aws.csv')
    print(df.to_string())
    return {"filename": df.to_json()}

@app.get("/data")
def read_root():
    # Send GET request to API endpoint
    url = "https://nodeumcu-clientserver.onrender.com/api/data"
    response = requests.get(url)

# Convert JSON response to DataFrame
    data = response.json() 
    df = pd.DataFrame(data)

# Append DataFrame to CSV file
    df.to_csv("data.csv", mode='a', header=False, index=False)
    df = pd.read_csv('data.csv')
    print(df.to_string())
    return {"data": df.to_json(orient="records")}




@app.get("/weather")
def read_root():
    raining = "Unknown"
    notRaining = "Unknown"
    if "rain" in wr.conditions.lower():
        print(f"It is currently raining in {wr.city}.")
        raining = f"It is currently raining in {wr.city}"
    else:
        print(f"It is not currently raining in {wr.city}.")
        notRaining = f"It is not currently raining in {wr.city}."
    city = wr.city
    temp = wr.temp
    hum = wr.hum
    windSpeed = wr.wind_speed
    compassDir = wr.compass_dir
    conditions = wr.conditions
    return {"city": city, "temp": temp, "hum": hum, "windSpeed": windSpeed, "compassDir": compassDir, "raining": raining,  "notRaining": notRaining, "conditions": conditions}
