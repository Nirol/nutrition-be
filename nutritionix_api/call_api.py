from nutritionix_api.settings import APP_ID, APP_KEY, INSTANT_SEARCH_ENDPOINT


def call_nutritionix_api(food_query: str):
    """
    This function calls the Nutritionix API and returns the results.
    """
    import requests
    import json


    headers = {
        "x-app-id": APP_ID,
        "x-app-key": APP_KEY,
    }

    query_params = {
        "query": food_query,
        "branded": "false",
        "common": "true",
        "common_general": "true",
        "detailed": "true",
    }

    # Set the URL

    # Call the API
    response = requests.get(url=INSTANT_SEARCH_ENDPOINT, params=query_params, headers=headers)

    # Convert the response to a Python dictionary
    data = json.loads(response.text)
    print(data)
    # Return the data
    return data