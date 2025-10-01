def safe_divide(numerator, denominator):
    """Performs safe division with error handling."""
    try:
        num = float(numerator)
        den = float(denominator)
        result = num / den
        return f"The result of the division is {result:.2f}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."
