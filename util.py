import pickle
import json
import numpy as np
import sklearn

__Make = None
__data_columns = None
__model = None

def get_Make_names():
    global __Make
    if __Make is None:
        load_saved_artifacts()  # Ensure data columns are loaded
        # Extract car makes from data columns
        __Make = []
        for column in __data_columns:
            if column.startswith("make_"):
                car_make = column.replace("make_", "").capitalize()
                __Make.append(car_make)
    return __Make

def load_saved_artifacts(json_file_path="./artifacts/columns.json"):
    global __data_columns
    global __model
    global __Make

    with open(json_file_path, "r") as f:
        __data_columns = json.load(f)['data_columns']
        print("Data columns loaded:", __data_columns)

    if __model is None:
        with open('./artifacts/Car_prices_model.pickle', 'rb') as f:
            __model = pickle.load(f)
            print("Model loaded successfully.")

def get_data_columns():
    return __data_columns

def get_estimated_price(Make, Year_of_manufacture, Engine_Size):
    try:
        loc_index = __data_columns.index(Make.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = Year_of_manufacture
    x[1] = Engine_Size

    if loc_index >= 0:
        x[loc_index] = 1

    return round(__model.predict([x])[0], 2)


if __name__ == '__main__':
    load_saved_artifacts()

    # Print the list of car makes
    for make in get_Make_names():
        print(make)

    # Test the get_estimated_price function
    print(get_estimated_price('Toyota', 2011.0, 4600.0))
    print(get_estimated_price('Lexus', 2011.0, 4600.0))
    print(get_estimated_price('Mercedes-Benz', 2011.0, 4600.0))
    print(get_estimated_price('Suzuki', 2011.0, 4600.0))
