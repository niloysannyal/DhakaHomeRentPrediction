import json
import pickle
import joblib
import numpy as np
import pandas as pd

__locations = None
__data_columns = None
__model = None

def get_estimated_rent(Location, Area_sqft, Bed, Bath):
    try:
        loc_index = __data_columns.index(Location)
    except ValueError:
        loc_index = -1

    input_data = {
        'Area_sqft': [Area_sqft],
        'Bed': [Bed],
        'Bath': [Bath]
    }

    for loc in __data_columns[3:]:  # Add all location columns
        input_data[loc] = [1 if loc == Location else 0]

    input_df = pd.DataFrame(input_data)

    # Ensure the columns are in the correct order
    input_df = input_df[__data_columns]

    return round(__model.predict(input_df)[0], 2)

def get_location_names():
    return __locations

def load_saved_artifacts():
    print("Loading saved artifacts...Start")
    global __locations, __data_columns, __model
    with open("./artifacts/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]

    __model = joblib.load("./artifacts/DhakaHomeRentPrediction.pkl")

    print("Loading saved artifacts...Done")

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())