import json
import requests

base_url = "https://archive-api.open-meteo.com/v1/archive"

def get_weather(lat, lon, start_date, end_date):
    params = {'latitude': lat,
              'longitude': lon,
              'start_date': start_date,
              'end_date': end_date,
              'hourly': 'temperature_2m,precipitation,wind_speed_10m',
              'timezone': 'America/New_York',
              'temperature_unit': 'fahrenheit',
              'wind_speed_unit': 'mph',
              'precipitation_unit': 'inch'
     }

    response = requests.get(base_url, params=params)
    response.raise_for_status()
    return response.json()

if __name__ == "__main__":
    data = get_weather(39.95, -75.17, "2025-10-01", "2026-09-30")
    print(len(data["hourly"]["time"]))
    print(data["hourly"]["time"][:3])
    print(data["hourly"]["temperature_2m"][:3])   
    print(data["hourly"]["precipitation"][:3]) 
    print(data["hourly"]["wind_speed_10m"][:3]) 

    with open("raw_weather.json", "w") as f: 
        json.dump(data, f)
    print("Saved raw_weather.json")