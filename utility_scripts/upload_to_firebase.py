from typing import Dict

from data.food_categories import CURRENT_VERSION, PARENT_COLLECTION
from firebase_manager import db
from models.food_nutrition import FoodNutrition


def upload_to_firebase(food_data:Dict):

    batch = db.batch()
    documents = {}
    for food_category in food_data.keys():
        collection_name = f'{PARENT_COLLECTION}/{CURRENT_VERSION}/{food_category.value.lower()}'
        for food_name in food_data[food_category].keys():
            food_nutrition_obj:FoodNutrition = food_data[food_category][food_name]
            food_dict = food_nutrition_obj.__dict__
            food_dict["id"] = food_nutrition_obj.food_name
            documents[food_nutrition_obj.food_name] = food_dict

            # save this food dict as doc into the the food category collection
            batch.set(db.collection(collection_name).document(food_dict["id"]), food_dict)


    batch.commit()