from utils.expense_calcualtor import Calculator
from langchain.tools import tool


class CalculatorTool():
    def __init__(self) -> None:
        self.calculation = Calculator()
        self.calculate = self._setup_tools()
    
    
    def _setup_tools(self):
        
        @tool
        def estimate_total_hotel_cost(price_per_night:str,total_days:int):
            """
            Calculate total hotel cost
            """
            
            return self.calculation.multiply(price_per_night,total_days)

        @tool        
        def calculate_total_expense(*costs:float):
            """calculate total expense in the trip"""
            
            return self.calculation.calculate_total(*costs)
        
        @tool
        def calculate_daily_expense_budget(total_cost:float,total_day:int)-> float:
            """
            calculate the daliy expense for the trip
            """
            return self.calculation.divide(total_cost,total_day)
        
        return [estimate_total_hotel_cost, calculate_total_expense, calculate_daily_expense_budget]
            