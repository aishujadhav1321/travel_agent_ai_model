from langchain.tools import tool

@tool
def estimate_budget(
    destination: str,
    days: int,
    travelers: int
) -> str:
    """
    Estimate travel budget.
    """

    hotel_cost = 4000 * days
    food_cost = 1500 * days * travelers
    misc = 3000

    total = hotel_cost + food_cost + misc

    return f"""
    Estimated budget for {destination}

    Hotel: ₹{hotel_cost}
    Food: ₹{food_cost}
    Misc: ₹{misc}

    Total Estimated Budget: ₹{total}
    """