from langchain.tools import tool

@tool
def places(city: str):
    """Get tourist places for a city"""
    return f"Top tourist places in {city}"