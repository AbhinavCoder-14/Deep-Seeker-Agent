class Calculator:
    @staticmethod
    def multiply(a: int, b: int) -> int:
        """
        Multiply two integers.

        Returns:
            int: The product of a and b.
        """
        return a * b
    
    @staticmethod
    def calculate_total(*x: float) -> float:
        """
        Calculate sum of the given list of numbers

        Returns:
            float: The sum of numbers in the list x
        """
        return sum(x)
    
    @staticmethod
    def calculate_daily_budget(total: float, days: int) -> float:
        """
        Calculate daily budget

        Returns:
            float: Expense for a single day
        """
        return total / days if days > 0 else 0
    
    