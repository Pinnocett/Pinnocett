from flask import Flask, request, jsonify
import util

app = Flask(__name__)


from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/get_Make_names', methods=['GET'])
def get_Make_names():
    response = jsonify({
        'Make': util.get_Make_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/predict_Make_price', methods=['GET', 'POST'])
def predict_Make_price():
    Year_of_manufacture = float(request.form['Year_of_manufacture'])
    Make = request.form['Make']
    Engine_Size = int(request.form['Engine_Size'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(Make, Year_of_manufacture, Engine_Size)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Car Price Prediction...")
    util.load_saved_artifacts()
    app.run()

