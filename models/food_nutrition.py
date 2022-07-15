
class FoodNutrition:
    """
    FoodNutrition class object.
    Contain the basic nutritional facts of the food, per 100g.
    """

    def __init__(self, food_name: str, carbs: float, fat: float, protein: float, calories: float):
        self.food_name = food_name
        self.carbs = carbs
        self.fat = fat
        self.protein = protein
        self.calories = calories

