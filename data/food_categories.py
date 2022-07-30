from enum import Enum

from data.food_lists.dairy import DAIRY_LIST
from data.food_lists.fruits import FRUITS_LIST
from data.food_lists.meat import MEAT_LIST
from data.food_lists.seafood import SEAFOOD_LIST
from data.food_lists.vegtabels import VEGETABLES_LIST


PARENT_COLLECTION = 'food_metadata'
CURRENT_VERSION = "1.0"


class FoodCategory(Enum):
    FRUITS = "Fruits"
    VEGETABLES = "Vegetables"
    DAIRY = "Dairy"
    MEAT = "Meat"
    SEAFOOD = "Seafood"




FOOD_CATEGORY_LIST = {
    FoodCategory.FRUITS: FRUITS_LIST,
    FoodCategory.VEGETABLES: VEGETABLES_LIST,
    FoodCategory.DAIRY: DAIRY_LIST,
    FoodCategory.MEAT: MEAT_LIST,
    FoodCategory.SEAFOOD: SEAFOOD_LIST
}