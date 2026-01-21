import os

from langchain.tools import tool
from utils.currency_converter import CurrencyConverter

class CurrencyConverterTool():
    def __init__(self) -> None:
        self.api_key = os.environ.get("OPENWEATHER_API_KEY")
        self.currencyconverter = CurrencyConverter(api_key=self.api_key)
        
        self.currencyConvertertool = self._setup_tools
    
    
    def _setup_tools(self):
        
        """
        Setup all tools for all the convertions of currency
        """
        
        
        @tool
        def convert(from_currency:str,to_currency:str,amount:float) -> float:
            """Convert the amount from one currency to another"""
            
            return self.currencyconverter.convert(amount,from_currency,to_currency)
        
        return [convert]