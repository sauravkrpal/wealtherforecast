import requests
import json
import pyttsx3



# Initialize text-to-speech engine
speaker = pyttsx3.init()

# Prompt the user for the city name
city = input("Enter the name of the city: ").strip()

# Get the weather data for the specified city
def get_weather(city):
    api_key = "fa512121d58c427b95e121246230112"
    url = f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
    response = requests.get(url)
    if response.status_code == 200:
        weather_data = json.loads(response.text)
        return weather_data
    else:
        print(f"Error: Failed to retrieve weather data. Code: {response.status_code}")
        return None

# Get and speak the weather data
weather_data = get_weather(city)
if weather_data:
    temperature_c = weather_data["current"]["temp_c"]
    city_name = weather_data["location"]["name"]
    text = f"The current temperature in {city_name} is {temperature_c} degrees Celsius."
    speaker.say(text)
    speaker.runAndWait()
else:
    print("Failed to retrieve weather data. Please try again.")
