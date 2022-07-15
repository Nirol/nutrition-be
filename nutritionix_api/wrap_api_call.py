from typing import Dict

from models.food_nutrition import FoodNutrition
from nutritionix_api.call_api import call_nutritionix_api
from nutritionix_api.parse_api_results import parse_nutritionix_api_results


def wrap_nutritionix_api_call(food_query: str) ->FoodNutrition:
    """
    the wrapping function for any nutritional fact api resource.
    the api resource used results will be parsed into the FoodNutrition class object first.

    Expected Arguments:
    food_query: the food query to search.
    """

    # using nutritionix api call
    raw_result:Dict = call_nutritionix_api(food_query)
    food_nutrition: FoodNutrition = parse_nutritionix_api_results(raw_result)
    return food_nutrition
