#Write a program that fetches and prints out a random Chuck Norris joke for the user. Use the API presented here:
# https://api.chucknorris.io/. The user should only be shown the joke text.
import requests
def get_chuck_norris_joke():
    url="https://api.chucknorris.io/jokes/random"
    response = requests.get(url)
    joke_data=(response.json())
    print(joke_data['value'])
get_chuck_norris_joke()


#Familiarize yourself with the OpenWeather weather API at: https://openweathermap.org/api. Your task is to write a
# program that asks the user for the name of a municipality and then prints out the corresponding weather condition
# description text and temperature in Celsius degrees. Take a good look at the API documentation. You must register
# for the service to receive the API key required for making API requests. Furthermore, find out how you can convert
# Kelvin degrees into Celsius.

from __init__ import weather_info

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def fetch_weather(city_name: str, api_token: str):
    url = f"{BASE_URL}?q={city_name}&appid={api_token}&units=metric"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as err:
        print(f"Error fetching weather data: {err}")
    return {}

def display_weather(weather_details: dict):
    if weather_details:
        try:
            condition = weather_details['weather'][0]['description']
            temperature = weather_details['main']['temp']
            print(f"Weather Condition: {condition}")
            print(f"Temperature: {temperature}°C")
        except (KeyError, IndexError) as e:
            print(f"Error parsing weather data: {e}")
    else:
        print("Failed to fetch weather data. Please try again.")

if __name__ == "__main__":
    api_key = weather_info()
    municipality = input("Enter the name of the municipality: ").strip()
    weather_data = fetch_weather(municipality, api_key)
    display_weather(weather_data)
