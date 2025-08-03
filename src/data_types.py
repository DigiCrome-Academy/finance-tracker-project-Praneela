
from datetime import datetime

def demonstrate_data_types() -> dict:
    """
    Demonstrates Python primitive data types.

    Returns:
        dict: A dictionary containing examples of each primitive type.
    """
    return {
        "integer": 42,
        "float": 3.14,
        "string": "Hello, Python!",
        "boolean": True,
        "none_type": None
    }

    
def add_numbers(a: int,b: int) -> int:
        return a + b

'''
'''
def multiply_floats(x: float,y: float) -> float:
    return x * y

def text_Uppercase(text: str) -> str:
    return text.upper()

def toggle_value(value: bool) -> bool:
    return not value

def currency_to_float(currency_str: str) -> float:
    try:
        currency_float = currency_str.replace("$","").replace(",","")
        return float(currency_float)
    except ValueError as e:
        raise ValueError(f"Invalid currency string : {str}") from e
   
def validate_date(date_str: str) -> bool:
    formats = ["%Y-%m-%d" ,"%d/%m/%Y", "%m-%d-%Y", "%B %d %Y"]
    for fmt in formats:
        try:
            datetime.strptime(date_str,fmt)
            return True
        except ValueError:
            continue
    return False
 
def calculate_percentage(part: float, total: float) -> float:
    if total == 0:
        raise ValueError("Cannot divide by Zero")
    return (part/total) * 100

def apply_percentage(value: float, percent:float) -> float:
    return value * (percent/100)
           
print(demonstrate_data_types())
print(f"Sum of Numbers: ",add_numbers(5,8))
print("Product of Numbers : ",multiply_floats(3.23,9.45))
print("String to Uppercase : ",text_Uppercase("Hello ,how are you ?"))
print("Toggle Boolean : ",toggle_value(False))
print("Convert currency string to float : ",currency_to_float("$1,234.56"))
print("Validate Date String :" ,validate_date("8/02/2025"))
print("Calculate Percentage : ",calculate_percentage(45,500))
print("Apply Percentage : ",apply_percentage(78,40))