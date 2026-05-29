from langchain.tools import tool

@tool
def search_flights(source: str, destination: str, date: str) -> str:
    """
    Search cheapest and fastest flights.
    """

    # Replace with Amadeus API integration

    return f"""
    Flights from {source} to {destination} on {date}

    Cheapest Flight:
    Indigo - ₹5400 - 2h 10m

    Fastest Flight:
    Air India - ₹7200 - 1h 45m
    """