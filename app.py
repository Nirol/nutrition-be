from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from starlette import status
from starlette.responses import JSONResponse

from food_data.get_food_data import get_food_data

import uvicorn

from models.food_nutrition import FoodNutrition


def create_server():
    app = FastAPI(
        title="routines-generator by Mirrori",
        description="Generate routines for free users",
        version="2.0.0",
        contact={"Name": "Nir Gilad", "url": "to be published", "email": "nirolgg@gmal.com"},
    )
    app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

    return app


app = create_server()


@app.get("/")
def hello_world():

    return "hello world :)"


@app.get("/food-value/{food_query}")
async def food_value(food_query: str):
    """
    This function calls the Nutritionix API for nutritional values,
     convert the data to 100g and return the results.
    Expected Arguments:
    food_query: the food id
    """
    food_data: FoodNutrition = get_food_data(food_query)
    item = {"message": "Generated guide and routines successfully", "food_query": food_query, "status": "success", "data": food_data.__dict__}
    return JSONResponse(status_code=status.HTTP_200_OK, content=item)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)