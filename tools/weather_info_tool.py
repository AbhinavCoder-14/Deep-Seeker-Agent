import os
import re
from typing import Any,Dict, List
from dotenv import load_dotenv
from langchain.tools import tool

from utils.weather_info import WeatherForcastTool




class WeatherInfoTool:
    
    def __init__(self):
        load_dotenv()
        self.api_key = os.environ.get("OPENWEATHER_API_KEY")
        self.weather_service = WeatherForcastTool(self.api_key)
        self.weather_tool_list = self._setup_tools()
        
    
    def _setup_tools(self)->List:
        """
        Setup all tools for the weather forecast tool
        """
        @tool
        def get_current_weather(city:str)->str:
            """Get current weather for a city"""
            
            weather_Data = self.weather_services.get_current_weather(city)
            if weather_Data:
                temp = weather_Data.get("main",{}).get("temp","N/A")
                desc = weather_Data.get("weather",[{}])[0].get("description","N/A")
                return f"Current weather of {city} is {temp}, {desc}"
            
            return f"count fetch the weather of {city}"
        
        
        
        @tool
        def get_weather_forecast(city:str):
            """Get Weather Forecast of the city"""
            
            forecast_Data = self.weather_service.get_forecast_weather(city)
            if(forecast_Data):
                pass
            
            
            
            
