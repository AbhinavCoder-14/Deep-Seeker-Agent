

import os
from pickletools import read_uint1
from langchain.tools import tool
from utils.place_info_search import GooglePlaceSearchTool,TavilyPlaceSearchTool



class PlaceSearchTool():
    def __init__(self) -> None:
        self.api_key_Gplace = os.environ.get("GPLACE_API_KEY")
        self.api_key_tavily = os.environ.get("TAVILY_API_KEY")
        
        self.place_search_tool = self._setup_tool
        
        self.googlePlaceSearchTool = GooglePlaceSearchTool(api_key=self.api_key_Gplace)
        self.tavilyPlaceSearchTool = TavilyPlaceSearchTool(api_key=self.api_key_tavily)
        
        
    
    
    def _setup_tool(self):
        """
        
        
        """

        @tool        
        def google_search_attractions(place:str):
            """
            Searches for attractions in the specified place using GooglePlaces API.
            """
            return self.googlePlaceSearchTool.google_search_activity(place)
          
        @tool    
        def google_search_restaurants(place:str):
            """
            Searches for available restaurants in the specified place using GooglePlaces API.
            """
            return self.googlePlaceSearchTool.google_search_restaurants(place)
            
            
        @tool
        def google_search_activity(place:str):
            """ Searches for popular activities in the specified place using GooglePlaces API."""
            
            return self.googlePlaceSearchTool.google_search_activity(place)
            
        @tool 
        def google_search_transportation(place:str):
            """

            Searches for available modes of transportation in the specified place using GooglePlaces API.
            """
            return self.googlePlaceSearchTool.google_search_transportation(place)
            
        @tool        
        def tavily_search_attractions(place:str):
            """
            Searches for attractions in the specified place using TavilySearch.
            """
            return self.tavilyPlaceSearchTool.tavily_search_activity(place)
          
        @tool    
        def tavily_search_restaurants(place:str):
            """
            Searches for available restaurants in the specified place using TavilySearch.
            """
            return self.tavilyPlaceSearchTool.tavily_search_restaurants(place)
            
            
        @tool
        def tavily_search_activity(place:str):
            """ Searches for popular activities in the specified place using TavilySearch."""
            
            return self.tavilyPlaceSearchTool.tavily_search_activity(place)
            
        @tool
        def tavily_search_transportation(place:str):
            """

            Searches for available modes of transportation in the specified place using TavilySearch.
            """
            return self.tavilyPlaceSearchTool.tavily_search_transportation(place)
            
        