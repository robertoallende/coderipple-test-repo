"""
Utility functions for CodeRipple test application.

This module provides mathematical and formatting utilities
to create meaningful code patterns for AI analysis.
"""

def calculate_fibonacci(n):
    """
    Calculate the nth Fibonacci number using iterative approach.
    
    Args:
        n (int): Position in Fibonacci sequence (0-indexed)
        
    Returns:
        int: The nth Fibonacci number
        
    Examples:
        >>> calculate_fibonacci(0)
        0
        >>> calculate_fibonacci(5)
        5
        >>> calculate_fibonacci(10)
        55
    """
    if n <= 1:
        return n
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    
    return b

def format_output(n, result):
    """
    Format the Fibonacci calculation result for display.
    
    Args:
        n (int): Input number
        result (int): Calculated Fibonacci number
        
    Returns:
        str: Formatted output string
    """
    return f"Fibonacci({n}) = {result}"

def validate_input(value):
    """
    Validate input for Fibonacci calculation.
    
    Args:
        value: Input value to validate
        
    Returns:
        bool: True if valid, False otherwise
        
    Raises:
        TypeError: If input is not an integer
        ValueError: If input is negative
    """
    if not isinstance(value, int):
        raise TypeError("Input must be an integer")
    
    if value < 0:
        raise ValueError("Input must be non-negative")
    
    return True

class FibonacciCalculator:
    """
    A class-based approach to Fibonacci calculations.
    
    Provides caching and additional functionality for
    more complex analysis patterns.
    """
    
    def __init__(self):
        """Initialize the calculator with empty cache."""
        self.cache = {}
    
    def calculate(self, n):
        """
        Calculate Fibonacci number with caching.
        
        Args:
            n (int): Position in sequence
            
        Returns:
            int: Fibonacci number
        """
        if n in self.cache:
            return self.cache[n]
        
        result = calculate_fibonacci(n)
        self.cache[n] = result
        return result
    
    def get_sequence(self, length):
        """
        Generate Fibonacci sequence up to specified length.
        
        Args:
            length (int): Number of terms to generate
            
        Returns:
            list: Fibonacci sequence
        """
        return [self.calculate(i) for i in range(length)]
