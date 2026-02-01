import requests

class WeatherForcastTool:
    def __init__(self, api_key: str):
        self.base_url = "https://api.openweathermap.org/data/2.5"
        self.api_key = api_key

    def get_current_weather(self, place: str):
        """Get current weather of a place"""
        url = f"{self.base_url}/weather"
        params = {
            "q": place,
            "appid": self.api_key,
            "units": "metric"
        }

        response = requests.get(url, params=params, timeout=10)

        if response.status_code == 200:
            return response.json()

        return {
            "error": "Failed to fetch current weather",
            "status_code": response.status_code,
            "response": response.text
        }

    def get_forecast_weather(self, place: str):
        """Get weather forecast of a place"""
        url = f"{self.base_url}/forecast"
        params = {
            "q": place,
            "appid": self.api_key,
            "cnt": 10,
            "units": "metric"
        }

        response = requests.get(url, params=params, timeout=10)

        if response.status_code == 200:
            return response.json()

        return {
            "error": "Failed to fetch forecast",
            "status_code": response.status_code,
            "response": response.text
        }
