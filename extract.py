import requests

base_url = "https://archive-api.open-meteo.com/v1/archive"

def get_weather(lat, lon, start_date, end_date):
    params = {'latitude': lat,
              'longitude': lon,
              'start_date': start_date,
              'end_date': end_date,
              'hourly': 'temperature_2m',
              'timezone': 'America/New_York'
     }

    response = requests.get(base_url, params=params)
    response.raise_for_status()
    return response.json()

if __name__ == "__main__":
    data = get_weather(39.95, -75.17, "2025-10-01", "2025-10-02")
    print(len(data["hourly"]["time"]))
    print(data["hourly"]["time"][:3])
    print(data["hourly"]["temperature_2m"][:3])
    
