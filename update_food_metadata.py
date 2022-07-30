from utility_scripts.get_food_data import get_food_data
from utility_scripts.upload_to_firebase import upload_to_firebase


if __name__ == '__main__':
    """
    query the nutritionix api for the updated food list
    save the data into a new metadata collection on the app firebase database.
    """


    # get the updated food list from the nutritionix api
    food_data = get_food_data()
    # save the data into a new metadata collection on the app firebase database.
    upload_to_firebase(food_data)