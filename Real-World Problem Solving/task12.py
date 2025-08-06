import requests
import os
from dotenv import load_dotenv
load_dotenv()

def fetch_weather_data(city="London"):
    """
    Fetches weather data for a given city using the OpenWeatherMap API.
    Returns parsed JSON data if successful, or None if an error occurs.
    """
    API_KEY=os.getenv('API_KEY') # importing from .env file for more security
    BASE_URL=os.getenv("BASE_URL")

    try:
        params = {
            'q': city,
            'appid': API_KEY,
            'units': 'metric'  # For Celsius temperature
        }
        response =requests.get(BASE_URL, params=params) #send get request to the API
        
        # Handle non-successful status codes
        if response.status_code != 200:
            print(f"Error: {response.status_code} - {response.reason}")
            try:
                error_data = response.json()
                print("Message:", error_data.get("message", "Unknown error"))
            except ValueError:
                print("Failed to decode error response.")
            return None

        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

def display_weather(data):
    """Displays weather data in a formatted way"""
    if not data:
        print("No weather data available.")
        return
    
    print("\nCurrent Weather:")
    print(f"City: {data['name']}, {data['sys']['country']}")
    print(f"Temperature: {data['main']['temp']}°C")
    print(f"Weather: {data['weather'][0]['description']}")
    print(f"Humidity: {data['main']['humidity']}%")
    print(f"Wind Speed: {data['wind']['speed']} m/s")

if __name__ == "__main__":
    city = input("Enter city name: ")
    weather_data = fetch_weather_data(city)
    display_weather(weather_data)
