import json
import pickle
import numpy as np

__locations = None
__data_columns = None
__model = None


def get_estimated_price(location, sqft, bhk, bath):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1    
    
    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    return round(__model.predict([x]) [0],2)

def get_data_columns():
    return __data_columns

def get_location_names():
    return __locations


def load_saved_Artifacts():
    print('loading saved artifacts. . .start')
    global __data_columns
    global __locations
    global __model
    import os

# Get the absolute path of the current script's directory
    script_directory = os.path.dirname(os.path.abspath(__file__))

# Construct the absolute path to columns.json
    columns_json_path = os.path.join(script_directory, "artifacts", "columns.json")

# Open the file
    with open(columns_json_path, 'r') as f:
    # Your file processing code here
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]


   # with open("./artifacts/columns.json", 'r') as f:
    #    __data_columns = json.load(f)['data_columns']
     #   __locations = __data_columns[3:]
import os

# Get the absolute path of the current script's directory
script_directory = os.path.dirname(os.path.abspath(__file__))

# Construct the absolute path to columns.json
house_price_path = os.path.join(script_directory, "artifacts", "bengaluru_house_price_prediction.pickle")

# Open the file
with open(house_price_path, 'rb') as f:

   # global __model
    #if __model is None:
       # with open('./artifacts/bengaluru_house_price_prediction.pickle', 'rb') as f:
    __model = pickle.load(f)
print('loading saved artifact. . .done')


if __name__ == '__main__':
    load_saved_Artifacts()
    print(get_location_names())
    print(get_estimated_price('1st Phase JP Nagar', 1000, 3, 3))
    print(get_estimated_price('Indira Nagar', 1000, 2, 2))
    print(get_estimated_price('Kalhalli', 1000, 2, 2)) # other location
    print(get_estimated_price('Ejipura', 1000, 2, 2))