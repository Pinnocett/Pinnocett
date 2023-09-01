from flask import Flask, request, jsonify
import os
import util

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Car Price Prediction API"

@app.route('/get_Make_names', methods=['GET', 'POST'])
def get_Make_names():
    response = jsonify({
        'Make': util.get_Make_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/predict_Make_price', methods=['POST'])
def predict_Make_price():
    data = request.get_json()

    Year_of_manufacture = float(data['Year_of_manufacture'])
    Make = data['Make']
    Engine_Size = int(data['Engine_Size'])

    estimated_price = util.get_estimated_price(Make, Year_of_manufacture, Engine_Size)

    response = jsonify({
        'estimated_price': estimated_price
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Car Price Prediction...")

    # Get the directory of the current script
    script_directory = os.path.dirname(os.path.abspath(__file__))

    # Construct the absolute path to the JSON file
    json_file_path = os.path.join(script_directory, "artifacts", "columns.json")

    print("JSON file path:", json_file_path)  # Print the file path

    util.load_saved_artifacts(json_file_path)  # Pass the JSON file path to the function
    app.run()
