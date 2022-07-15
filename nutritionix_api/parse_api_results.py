from typing import Dict, List

from models.food_nutrition import FoodNutrition
from nutritionix_api.constants import ATTRIBUTE_ID_LIST, CARBOHYDRATE_ATTRIBUTE_ID, FAT_ATTRIBUTE_ID, \
    PROTEIN_ATTRIBUTE_ID, ENERGY_KCAL_ATTRIBUTE_ID


def _create_food_nutrition_object(food_name: str,nutrients_list:List[Dict]):
    """
    This function creates a FoodNutrition object from the parsed results.
    :param food_name:
    :param nutrients_list:
    :return:
    """



    carbs = next(nutrient["value"] for nutrient in nutrients_list if nutrient["attr_id"] == CARBOHYDRATE_ATTRIBUTE_ID)
    fat = next(nutrient["value"] for nutrient in nutrients_list if nutrient["attr_id"] == FAT_ATTRIBUTE_ID)
    protein = next(nutrient["value"] for nutrient in nutrients_list if nutrient["attr_id"] == PROTEIN_ATTRIBUTE_ID)
    calories = next(nutrient["value"] for nutrient in nutrients_list if nutrient["attr_id"] == ENERGY_KCAL_ATTRIBUTE_ID)

    # create a FoodNutrition object
    food_nutrition = FoodNutrition(food_name=food_name,
                                  carbs=carbs,
                                  fat=fat,
                                  protein=protein,
                                  calories=calories)
    return food_nutrition

def _convert_to_100g(nutrients_list, serving_size_in_grams):
    for nutrient in nutrients_list:
        nutrient["value"] = nutrient["value"] / (serving_size_in_grams / 100)

def _extract_supported_nutrients(ingredients:List[Dict]):
    """
    The currently supported nutrients can be found under constants.
    :param food_result:
    :return:
    """

    return list(filter(lambda ingredient: ingredient['attr_id'] in ATTRIBUTE_ID_LIST, ingredients))


def parse_nutritionix_api_results(results:Dict) ->FoodNutrition:
    """
    This function parses the results from the Nutritionix API and returns the results.
    Example raw results:
    {
    "message": "Generated guide and routines successfully",
    "food_query": "celery",
    "status": "success",
    "data": {
        "common": [
            {
                "food_name": "celery",
                "serving_unit": "stalk",
                "tag_name": "celery",
                "serving_qty": 1,
                "common_type": null,
                "tag_id": "15733",
                "serving_weight_grams": 37.5,
                "full_nutrients": [
                    {
                        "value": 0.3113,
                        "attr_id": 203
                    },
                    {
                        "value": 0.06,
                        "attr_id": 204
                    },
                    {
                        "value": 1.5,
                        "attr_id": 205
                    },
                    ...

                ],
                "photo": {
                    "thumb": "https://d2eawub7utcl6.cloudfront.net/images/nix-apple-grey.png",
                    "highres": null,
                    "is_user_uploaded": false
                },
                "locale": "en_US"
            },
            {
                "food_name": "raw celery",
                "serving_unit": "stalk",
                "tag_name": "celery",
                "serving_qty": 1,
                "common_type": null,
                "tag_id": "15733",
                "serving_weight_grams": 37.5,
                "full_nutrients": [ ...
                ],
                "photo": {
                    "thumb": "https://d2eawub7utcl6.cloudfront.net/images/nix-apple-grey.png",
                    "highres": null,
                    "is_user_uploaded": false
                },
                "locale": "en_US"
            },
            ...
        ]
    }
}
    """

    # grab the first common food result
    food_result = results["common"][0]
    serving_size_in_grams = food_result["serving_weight_grams"]
    nutrients_list = _extract_supported_nutrients(food_result["full_nutrients"])
    _convert_to_100g(nutrients_list, serving_size_in_grams)
    return _create_food_nutrition_object(food_name= food_result["food_name"],nutrients_list=nutrients_list)



