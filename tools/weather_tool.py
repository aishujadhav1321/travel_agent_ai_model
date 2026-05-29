from langchain.tools import tool

@tool
def weather(city: str):
    """Get weather for a city"""
    
    return f"Weather in {city} is sunny"