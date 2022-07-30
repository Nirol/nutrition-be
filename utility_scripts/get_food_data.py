import time

from data.food_categories import FOOD_CATEGORY_LIST
from models.food_nutrition import FoodNutrition
from nutritionix_api.wrap_api_call import wrap_nutritionix_api_call


def get_food_data():
    """
    query the nutritionix api for the updated food list

    """
    # get the updated food list from the nutritionix api
    food_data = {}
    for food_category in FOOD_CATEGORY_LIST.keys():
        food_data[food_category] = {}
        for food_name in FOOD_CATEGORY_LIST[food_category]:

            food_nutrition: FoodNutrition = wrap_nutritionix_api_call(food_query=food_name)

            food_data[food_category][food_name] = food_nutrition
            # add some sleep time to not overload the api accesse quota to the nutritionix api
            time.sleep(5)

    return food_data
