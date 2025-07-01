#!/usr/bin/env python3
"""
CodeRipple Test Application

A simple Python application designed to trigger meaningful AI analysis
for testing the CodeRipple automated documentation system.
"""

import sys
from utils import calculate_fibonacci, format_output

def main():
    """
    Main application entry point.
    
    Demonstrates basic functionality for CodeRipple analysis:
    - Command line argument processing
    - Function calls and data flow
    - Error handling patterns
    """
    if len(sys.argv) != 2:
        print("Usage: python main.py <number>")
        sys.exit(1)
    
    try:
        n = int(sys.argv[1])
        if n < 0:
            raise ValueError("Number must be non-negative")
        
        result = calculate_fibonacci(n)
        output = format_output(n, result)
        print(output)
        
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

def demo_functionality():
    """
    Demonstrate application functionality with sample data.
    
    This function provides examples of the application's capabilities
    for documentation and testing purposes.
    """
    print("CodeRipple Test Application Demo")
    print("=" * 35)
    
    # Test cases for analysis
    test_cases = [0, 1, 5, 10, 15]
    
    for n in test_cases:
        result = calculate_fibonacci(n)
        output = format_output(n, result)
        print(output)

if __name__ == "__main__":
    main()
