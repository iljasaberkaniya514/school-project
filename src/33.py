import requests
from bs4 import BeautifulSoup

def fetch_weather_data(city_name):
    url = f"https://weather.com/weather/chance/t/forecast/{city_name}/"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        weather_data = soup.find("div", class_="BNeawe").find_all("div", class_="lbp")
        return weather_data[1].text
    else:
        return "Failed to fetch data"

city_name = input("Enter the name of the city: ")
weather_data = fetch_weather_data(city_name)
print(f"The current weather in {city_name} is: {weather_data}")
