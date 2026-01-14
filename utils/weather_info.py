import requests
from urllib3 import request, response

class WeatherForcastTool:
    def __init__(self,api_key:str):
        self.base_url = "https://api/openweathermap.org/data/2.5"
        self.api_key = api_key
        pass
    
    def get_current_weather(self,place:str):
        """Get current weather of a place"""
        try:
            url = f"{self.base_url}/weather"
            params = {
                "q":place,
                "appid":self.api_key,
            }
            response = requests.get(url,params=params)
            if(response.status_code==200):
                return response.json()
            
        except Exception as e:
            raise e
        
        
    def get_forecast_weather(self,place:str):
        """
        get weather forecast of a place        
        """
        try:
            url = f"{self.base_url}/forecast"
            params = {
                "q":place,
                "appid":self.api_key,
                "cnt":10,
                "units":"metric",
                }
            response = requests.get(url,params=params)
            
            if(response.status_code==200):
                return response.json()
            
        except Exception as e:
            raise e