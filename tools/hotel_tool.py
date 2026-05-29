from langchain.tools import tool

@tool
def search_hotels(city: str) -> str:
    """
    Search hotels in a city.
    """

    return f"""
    Top hotels in {city}

    1. Grand Palace Hotel - ₹4500/night
    2. Comfort Stay - ₹3200/night
    3. Luxury Residency - ₹7200/night
    """