from models.food_nutrition import FoodNutrition
from nutritionix_api.wrap_api_call import wrap_nutritionix_api_call


def get_food_data(food_query: str) ->FoodNutrition:
    """
    the wrapping function for any nutritional fact api resource.
    the api resource used results will be parsed into the FoodNutrition class object first.

    Expected Arguments:
    food_query: the food query to search.
    """

    # using nutritionix api call
    food_data: FoodNutrition = wrap_nutritionix_api_call(food_query)

    return food_data