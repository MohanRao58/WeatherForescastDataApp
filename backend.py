import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access the API key
API_KEY = os.getenv('API_KEY')
#print(api_key)  # Use your API key in your code



def get_data(place, forecast_days=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]
    return filtered_data


if __name__ == "__main__":
    print(get_data(place="Tokyo", forecast_days=3))