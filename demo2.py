# my_code.py (Example code to test)

def calculate_discount(price: float, discount_percentage: float) -> float:
    """Calculates the discounted price.

    Args:
        price: The original price.
        discount_percentage: The discount percentage (0-100).

    Raises:
        ValueError: If the price is negative or the discount percentage is invalid.

    Returns:
        The discounted price.
    """
    if price < 0:
        raise ValueError("Price cannot be negative.")
    if not 0 <= discount_percentage <= 100:
        raise ValueError("Discount percentage must be between 0 and 100.")

    discount_amount = price * (discount_percentage / 100)
    return price - discount_amount


def format_address(street: str, city: str, state: str, zip_code: str, country: str = "USA") -> str:
    """Formats an address string.

    Args:
        street: The street address.
        city: The city.
        state: The state.
        zip_code: The zip code.
        country: The country (default is "USA").

    Returns:
        A formatted address string.
    """
    address_parts = [street, city, state, zip_code, country]
    formatted_address = ", ".join(part for part in address_parts if part)  # Join with commas, skip empty parts
    return formatted_address


def process_data(data: list, operation: str = "sum") -> float:
    """Processes a list of numbers.

    Args:
        data: A list of numbers.
        operation: The operation to perform ("sum", "average", "max", "min").

    Raises:
        ValueError: If the operation is invalid or the data list is empty.
        TypeError: If the elements in the data list are not numbers

    Returns:
        The result of the operation.
    """

    if not data:
        raise ValueError("Data list cannot be empty.")

    if not all(isinstance(x, (int, float)) for x in data):
        raise TypeError("All elements in the data list must be numbers.")

    if operation == "sum":
        return sum(data)
    elif operation == "average":
        return sum(data) / len(data)
    elif operation == "max":
        return max(data)
    elif operation == "min":
        return min(data)
    else:
        raise ValueError("Invalid operation. Choose from 'sum', 'average', 'max', 'min'.")


# Example usage (you can add more complex code here)
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def apply_discount(self, discount_percentage):
        return calculate_discount(self.price, discount_percentage)
